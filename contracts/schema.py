from datetime import date, datetime
from typing import Any, Generic, List, Optional, Type, Union
from pydantic import BaseModel, validator



def confirm_address(value: str) -> str:
    if not value:
        raise ValueError("Please counterpart address.")
    return value

def confirm_contract_id(value: str) -> str:
    if not value:
        raise ValueError("Please contract id.")
    return value


class ContractBase(BaseModel):
    contract_id: str 
    counterpart_address: str
    _confirm_contract_id = validator("contract_id", allow_reuse=True)(confirm_contract_id)
    _confirm_counterpart_address = validator("counterpart_address", allow_reuse=True)(confirm_address)

class CreateContract(ContractBase):
   pass

class UpdateContract(ContractBase):
   pass


class ContractOut(ContractBase):
    class Config:
        orm_mode = True

class ContractListOut(BaseModel):
    class Config:
        orm_mode = True

