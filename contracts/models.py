from datetime import date, datetime 
from pathlib import Path 
from typing import Any, Callable, List, Union 
from django.conf import settings 
from django.db import models 
from pydantic import AnyUrl 
from contracts.managers import ContractManager


class Contract(models.Model):
    user: Any = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, null=True, on_delete=models.SET_DEFAULT, related_name="posts")
    contract_id: str = models.CharField(max_length=250)
    counterpart_address: str = models.TextField(null=True, blank=True)
    updated_at: datetime = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_at: datetime = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects: ContractManager = ContractManager()

    class Meta:
        verbose_name: str = "contract"
        verbose_name_plural: str = "contracts"
        ordering: list = ["-id"]

    def __repr__(self) -> str:
        return "<Post %r>" % self.title

    def __str__(self) -> str:
        return f"{self.title}"