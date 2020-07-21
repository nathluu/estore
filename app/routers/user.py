from fastapi import APIRouter
import sqlalchemy as db
from sqlalchemy import orm

from app.database.sql import SqlDbConnection
from app.user.dto import UserDtoIn, UserDtoOut
from app.user.repo import UserRepo

router = APIRouter()
user_repo: UserRepo = None


@router.on_event("startup")
async def init_user_repo():
    conn = SqlDbConnection("sqlite:///estore.db")
    global user_repo
    user_repo = UserRepo(conn.session)
    pass


@router.get("/users/")
async def get_users():
    pass


@router.get("/users/{user_id}")
async def get_user(user_id: int):
    pass


@router.post("/users/")
async def create_user(user: UserDtoIn):
    user_id = user_repo.save(user)
    return UserDtoOut(user_id=user_id)


@router.put("/users/{user_id}")
async def update_user(user_id: int):
    pass
