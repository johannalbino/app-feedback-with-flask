from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from src.db.crud import get_all_users, get_user_by_nickname, create_user
from src.db.database import SessionLocal
from src.db.schemas import User, UserCreate


user_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user_router.get('/users/', response_model=List[User], response_class=JSONResponse)
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_all_users(db, skip, limit)
    return users


@user_router.post('/users/', response_model=User, response_class=JSONResponse)
async def create_users(user: UserCreate, db: Session = Depends(get_db)):
    nickname_exists = get_user_by_nickname(db, user.nickname)
    if nickname_exists is None:
        return create_user(db=db, user=user)
    raise HTTPException(status_code=400, detail='Nickname already registered!')
