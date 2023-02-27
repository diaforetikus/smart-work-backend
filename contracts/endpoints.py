from typing import Any, List
from fastapi import APIRouter
from contracts.api_crud import contract
from contracts.schema import (ContractOut, ContractListOut, CreateContract, UpdateContract)

router = APIRouter()

@router.get("/", response_model=List[ContractListOut])
def get_contracts(offset: int = 0, limit: int = 10) -> Any:
	"""
	Endpoint to get multiple contracts based on offset and limit values.
	"""
	return contract.get_multiple(offset=offset, limit=limit)

@router.post("/", status_code=201, response_model=CreateContract)
def create_contract(request: CreateContract) -> Any:
	"""
	Endpoint to create a single contract.
	"""
	return contract.create(obj_in=request)


@router.put("/{pk}/", response_model=UpdateContract)
def update_contract(pk: int, request: UpdateContract) -> Any:
	"""
	Update a single contract.
	"""
	return contract.update(pk=pk, obj_in=request)


@router.delete("/{pk}/")
def delete_post(pk: int) -> Any:
	"""
	Delete a single contract.
	"""
	return contract.delete(pk=pk)

