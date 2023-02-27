from typing import Any, List
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder
from users.schema import (BaseUser, RegUser,
                          ResetPassword, UpdateUserBio, UpdateUserEmail, UpdateChangePassword)
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.utils import IntegrityError
from jose import jwt, JWTError


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def generate_token(user: BaseUser):
    token_data = jsonable_encoder({
        'id': user.id,
        'email': user.email,
    })
    return jwt.encode(token_data, 'secret', algorithm='HS256')


def get_current_user(token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        token_data = jwt.decode(token, 'secret', algorithms=['HS256'])

        email: str = token_data.get("email")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = User.objects.filter(email=email, is_active=True).first()

    if user is None:
        raise credentials_exception

    return user


@router.get("/")
def get_user() -> Any:
    return {"succes": True}


@router.post("/sign-up/")
def sign_up(request: RegUser) -> Any:

    data = request

    if User.objects.filter(email=data.email).exists():
        raise HTTPException(status_code=404, detail="User already exists")

    data.password = make_password(data.password)

    data = jsonable_encoder(data)
    data["username"] = data["email"]
    data["is_active"] = True

    try:
        user = User.objects.create(**data)
    except:
        raise HTTPException(status_code=404, detail="Error occured")

    return {
        "id": user.id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "account": None,
        "balance": 0,
        "token": generate_token(user),
    }


@router.post("/token/")
def token(data: OAuth2PasswordRequestForm = Depends()):

    user = authenticate(username=data.username, password=data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token_data = jsonable_encoder({
        'id': user.id,
        'email': user.email,
    })

    token = jwt.encode(token_data, 'secret', algorithm='HS256')

    return {"access_token": token, "token_type": "bearer"}


@router.post("/sign-in/")
def sign_in(data: OAuth2PasswordRequestForm = Depends()):

    user = authenticate(username=data.username, password=data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {
        "id": user.id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "account": None,
        "balance": 0,
        "token": generate_token(user),
    }


@router.post("/reset-password/")
def reset_password(data: ResetPassword) -> Any:

    user = User.objects.filter(email=data.email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User doesn't exist",
        )

    return {"success": True}


@router.patch("/update-bio")
def update_bio(data: UpdateUserBio, current_user: User = Depends(get_current_user)) -> Any:

    data = jsonable_encoder(data)

    user = User.objects.filter(id=current_user.id).update(**data)

    return {"success": True}


@router.patch("/update-email")
def update_email(data: UpdateUserEmail, current_user: User = Depends(get_current_user)) -> Any:
    if current_user.email != data.email:
        if User.objects.filter(email=data.email).exists():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=[{"loc": ["body", "email"],
                         "msg": "User with this email already exist"}],
            )

        current_user.email = data.email
        current_user.username = data.email
        current_user.save()

    return {
        "id": current_user.id,
        "email": current_user.email,
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "token": generate_token(current_user),
    }


@router.post("/change-password")
def change_password(data: UpdateChangePassword, current_user: User = Depends(get_current_user)) -> Any:

    user = authenticate(username=current_user.username, password=data.password)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=[
                {"loc": ["body", "password"], "msg": "Wrong password"}],
        )

    current_user.password = make_password(data.new_password)
    current_user.save()

    return {"success": True}


@router.get("/me/", response_model=BaseUser, dependencies=[Depends(get_current_user)])
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
