from datetime import date, datetime
from typing import Any, Generic, List, Optional, Type, Union
from pydantic import BaseModel, Field, EmailStr, validator
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async


def check_email(value: str) -> str:

    is_exists = sync_to_async(User.objects.filter(email=value).exists())
    if is_exists:
        raise ValueError("User arleady exists.")
    return value


class BaseUser(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str 
    token: str

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    class Config:
        orm_mode = True


class UpdateUserEmail(BaseModel):
    email: EmailStr


class UpdateUserBio(BaseModel):
    first_name: str = Field(min_length=2, max_length=50)  
    last_name: str = Field(min_length=2, max_length=50)


class UpdateChangePassword(BaseModel):
    password: str = Field(min_length=6, max_length=50)  
    new_password: str = Field(min_length=6, max_length=50)
    

class RegUser(BaseModel):
    email: EmailStr
    first_name: str = Field(min_length=2, max_length=50)  
    last_name: str = Field(min_length=2, max_length=50) 
    password: str = Field(min_length=6, max_length=50)
    #_check_email = validator("email", allow_reuse=True)(check_email)


class ResetPassword(BaseModel):
    email: EmailStr


    


