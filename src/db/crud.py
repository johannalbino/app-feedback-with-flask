from sqlalchemy.orm import Session
from src.models import User, Address
import src.db.schemas as schemas


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_address(db: Session, address: str):
    return db.query(Address).filter(Address.email_address == address).first()


def get_user_by_nickname(db: Session, nickname: str):
    return db.query(User).filter(User.nickname == nickname).first()


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(
        name=user.name,
        fullname=user.fullname,
        nickname=user.nickname
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_address(db: Session, skip: int = 0, limit: int = 0):
    return db.query(Address).offset(skip).limit(limit).all()


def create_user_address(db: Session, address: schemas.AddressCreate, user_id: int):
    db_address = Address(
        **address.dict(),
        user_id=user_id
    )
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

