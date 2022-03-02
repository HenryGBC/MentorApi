from sys import prefix
from fastapi import APIRouter
from pydantic import BaseModel
from tortoise.contrib.fastapi import HTTPNotFoundError
from .models import Mentor
from tortoise.contrib.pydantic import pydantic_model_creator

class IMentor(BaseModel):
    name: str
    username: str
    bio: str



Mentor_pydantic = pydantic_model_creator(Mentor, name="Mentor")

router = APIRouter(
    prefix='/mentors',
    tags=['mentors'],
    responses={404: {"description": "Not found"}},
)

@router.get('/')
async def get_mentors():
    return await Mentor_pydantic.from_queryset(Mentor.all())   



@router.post('/create', responses={404: {"model": HTTPNotFoundError}})
async def create_mentors(mentor: IMentor):
    mentor_obj = await Mentor.create(**mentor.dict(exclude_unset=True))
    return{
        "name":  mentor_obj.name,
        "username":  mentor_obj.username,
        "bio":  mentor_obj.bio
    }