from datetime import date, datetime 
from pathlib import Path 
from typing import Any, Callable, List, Union 
from django.conf import settings 
from django.db import models 
from pydantic import AnyUrl 


JOB_STATUSES = (
    (1, "open"),
    (2, "waiting"),
    (3, "at work"),
    (4, "completed"),
    (5, "canceled"),
)

PROPOSAL_STATUSES = (
    (1, "waiting"),
    (2, "accepted"),
)


class JobCategory(models.Model):
    name: str = models.CharField(max_length=250)
    updated_at: datetime = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_at: datetime = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name: str = "category"
        verbose_name_plural: str = "categories"
        ordering: list = ["-id"]

    def __repr__(self) -> str:
        return "<Category %r>" % self.name

    def __str__(self) -> str:
        return f"{self.name}"


class Job(models.Model):
    owner: Any = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, null=True, on_delete=models.SET_DEFAULT, related_name="my_jobs_set")
    executor: Any = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, null=True, on_delete=models.SET_DEFAULT)
    category: JobCategory = models.ForeignKey(JobCategory, default=None, null=True, on_delete=models.SET_DEFAULT)
    title: str = models.CharField(max_length=250)
    description: str = models.TextField()
    amount: int = models.PositiveIntegerField()
    contract_id: str = models.CharField(max_length=250)
    executor_address: str = models.CharField(max_length=250, null=True, default="")
    status_id: int = models.PositiveSmallIntegerField(default=1, choices=JOB_STATUSES)
    updated_at: datetime = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_at: datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    assigned_at: datetime = models.DateTimeField(null=True)
    started_at: datetime = models.DateTimeField(null=True)
    completed_at: datetime = models.DateTimeField(null=True)

    class Meta:
        verbose_name: str = "job"
        verbose_name_plural: str = "jobs"
        ordering: list = ["-id"]

    def __repr__(self) -> str:
        return "<Job %r>" % self.title

    def __str__(self) -> str:
        return f"{self.title}"

    @property
    def status(self):
        return dict(JOB_STATUSES).get(self.status_id)


class Proposal(models.Model):
    user: Any = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, null=True, on_delete=models.CASCADE)
    job: Job = models.ForeignKey(Job, on_delete=models.CASCADE)
    text: str = models.TextField()
    address: str = models.CharField(max_length=250, null=True, default="")
    status_id: int = models.PositiveSmallIntegerField(default=1, choices=PROPOSAL_STATUSES)
    updated_at: datetime = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_at: datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    accepted_at: datetime = models.DateTimeField(null=True)

    class Meta:
        verbose_name: str = "proposal"
        verbose_name_plural: str = "proposals"
        ordering: list = ["id"]

    def __repr__(self) -> str:
        return "<Job %r>" % self.text

    def __str__(self) -> str:
        return f"{self.text}"

    @property
    def status(self):
        return dict(PROPOSAL_STATUSES).get(self.status_id)