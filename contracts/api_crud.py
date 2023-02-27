from typing import Generic, List, Optional, Type, TypeVar
from unicodedata import category
from smart_work.base_crud import BaseCRUD
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model, Prefetch, query
from fastapi import Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from contracts.models import Contract
from contracts.schema import CreateContract, UpdateContract



class ContractCRUD(BaseCRUD[Contract, CreateContract, UpdateContract]):
	"""
	CRUD Operation for blog categories.
	"""

	def get(self, pk: int) -> Optional[Contract]:
		"""
		Get a single category.
		"""
		try:
			query = Contract.objects.pk(slug=pk)
			return query
		except ObjectDoesNotExist:
			raise HTTPException(status_code=404, detail="This contract does not exists.")

	def get_multiple(self, limit:int = 100, offset: int = 0) -> List[Contract]:
		"""
		Get multiple contracts using a query limiting flag.
		"""
		query = Contract.objects.all()[offset:offset+limit]
		if not query:
			raise HTTPException(status_code=404, detail="There are no contracts.")
		return list(query)

	def create(self, obj_in: CreateContract) -> Contract:
		"""
		Create a contract.
		"""
		obj_in = jsonable_encoder(obj_in)
		query = Contract.objects.create(**obj_in)
		return query

	def update(self, obj_in: UpdateContract, pk: int) -> Contract:
		"""
		Update a contract.
		"""
		if not isinstance(obj_in, list):
			obj_in = jsonable_encoder(obj_in)

		return self.model.objects.filter(pk=pk).update(**obj_in)

	def delete(self, pk: int) -> Contract:
		"""Delete a contract."""
		Contract.objects.filter(pk=pk).delete()
		return {"detail": "Successfully deleted!"}
		

contract = ContractCRUD(Contract)
