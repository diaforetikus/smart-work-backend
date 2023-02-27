from datetime import date, datetime
from typing import Any, Generic, List, Optional, Type
from pydantic import BaseModel, Field
from jobs.models import JobCategory
from users.schema import User


class JobCategory(BaseModel):
    id: int  
    name: str
    class Config:
        orm_mode = True


class JobAdd(BaseModel):
    title: str = Field(min_length=5, max_length=255)  
    description: str = Field(min_length=5, max_length=5000)
    amount: int = Field(..., min=1)  
    category_id: int = Field(..., min=1)  


class JobOut(BaseModel):
    id: int
    title: str  
    description: str
    amount: int
    category: JobCategory
    owner: User
    executor: User | None
    status: str
    contract_id: str
    created_at: datetime
    assigned_at: datetime | None
    started_at: datetime | None
    completed_at: datetime | None

    class Config:
        orm_mode = True


class JobListOut(JobOut):
    class Config:
        orm_mode = True


class ProposalAdd(BaseModel):
    text: str = Field(min_length=5, max_length=2000)  
    address: str = Field(min_length=42, max_length=100)


class ProposalAccept(BaseModel):
    contract_id: str = Field(min_length=1, max_length=100)


class ProposalOut(BaseModel):
    id: int
    job_id: int
    text: str  
    address: str
    user: User
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
