from contracts.endpoints import router as contracts_router
from users.endpoints import router as users_router
from jobs.endpoints import router as jobs_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(contracts_router, prefix="/contracts", tags=["Contracts"])
router.include_router(users_router, prefix="/users", tags=["Users"])
router.include_router(jobs_router, prefix="/jobs", tags=["Jobs"])