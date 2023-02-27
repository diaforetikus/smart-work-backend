from typing import Any, List
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.encoders import jsonable_encoder
from jobs.schema import (JobAdd, JobOut, ProposalAdd, ProposalOut, ProposalAccept)
from django.contrib.auth.models import User
from users.endpoints import get_current_user
from jobs.models import Job, Proposal
import datetime


router = APIRouter()

@router.post("", response_model=JobOut)
def add_job(job: JobAdd, current_user: User = Depends(get_current_user)) -> JobOut:

    job = jsonable_encoder(job)
    job["owner"] = current_user

    job = Job.objects.create(**job)

    return job

@router.get("/{pk:int}", response_model=JobOut)
def get_job(pk: int) -> JobOut:

    job = Job.objects.filter(pk=pk).first()

    return job


@router.get("", response_model=list[JobOut])
def jobs_list(category_id: int | None = None) -> list[JobOut]:


    filter = {
        "status_id": 1
    }

    if category_id:
        filter["category_id"] = category_id

    jobs = list(Job.objects.filter(**filter))

    return jobs





@router.get("/my", response_model=list[JobOut])
def my_jobs_list(category_id: int | None = None, status_id: int | None = None, current_user: User = Depends(get_current_user)) -> list[JobOut]:

    filter = {
        "owner": current_user
    }

    if category_id:
        filter["category_id"] = category_id

    if status_id:
        filter["status_id"] = status_id

    jobs = list(Job.objects.filter(**filter))

    return jobs


@router.get("/worklist", response_model=list[JobOut])
def worklist(category_id: int | None = None, status_id: int | None = None, current_user: User = Depends(get_current_user)) -> list[JobOut]:

    job_ids = Proposal.objects.filter(user=current_user).values_list('job_id', flat=True)

    filter = {
        'id__in': job_ids
    }

    if category_id:
        filter["category_id"] = category_id

    if status_id:
        filter["status_id"] = status_id

    jobs = list(Job.objects.filter(**filter))

    return jobs


@router.get("/{pk:int}/proposals", response_model=list[ProposalOut])
def get_proposals(pk: int, current_user: User = Depends(get_current_user)) -> list[ProposalOut]:

    job = Job.objects.filter(pk=pk).first()

    filter = {
        "job_id": pk
    }

    if current_user.id != job.owner.id:
        filter["user_id"] = current_user.id

    proposals = list(Proposal.objects.filter(**filter))

    return proposals


@router.post("/{pk:int}/proposals", response_model=ProposalOut)
def add_proposal(pk: int, proposal: ProposalAdd, current_user: User = Depends(get_current_user)) -> ProposalOut:

    proposal = jsonable_encoder(proposal)
    proposal["job_id"] = pk
    proposal["user"] = current_user

    proposal = Proposal.objects.create(**proposal)

    return proposal


@router.post("/{pk:int}/proposals/accept/{proposal_id:int}", response_model=ProposalOut)
def accept_proposal(pk: int, proposal_id: int, data: ProposalAccept, current_user: User = Depends(get_current_user)) -> ProposalOut:

    proposal = Proposal.objects.filter(id=proposal_id).first()
    proposal.status_id = 2
    proposal.accepted_at = datetime.datetime.now()
    proposal.save()

    job = Job.objects.filter(pk=pk, owner=current_user).first()
    job.status_id = 2
    job.executor = proposal.user
    job.contract_id = data.contract_id
    job.executor_address = proposal.address
    job.assigned_at = proposal.accepted_at
    job.save()

    return proposal


@router.post("/{job_id:int}/proposals/cancel", response_model=JobOut)
def cancel_proposal(job_id: int, current_user: User = Depends(get_current_user)) -> JobOut:

    proposal = Proposal.objects.filter(job_id=job_id, status_id=2).first()
    proposal.status_id = 1
    proposal.accepted_at = None
    proposal.save()

    job = Job.objects.filter(pk=job_id, owner=current_user).first()
    job.status_id = 1
    job.executor = None
    job.contract_id = ''
    job.executor_address = ''
    job.assigned_at = None
    job.save()

    return job


@router.post("/{pk:int}/accept", response_model=JobOut)
def accept(pk: int, current_user: User = Depends(get_current_user)) -> JobOut:
    job = Job.objects.filter(pk=pk, executor=current_user).first()
    job.started_at = datetime.datetime.now()
    job.status_id = 3
    job.save()

    return job


@router.post("/{pk:int}/complete", response_model=JobOut)
def complete(pk: int, current_user: User = Depends(get_current_user)) -> JobOut:
    job = Job.objects.filter(pk=pk, owner=current_user).first()
    job.completed_at = datetime.datetime.now()
    job.status_id = 4
    job.save()

    return job
