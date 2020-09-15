from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Boolean
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from .db.base_class import Base
from src.settings import DatabasePSQL

db = DatabasePSQL.session_database()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    created = Column(DateTime, default=datetime.utcnow())
    updated = Column(DateTime, default=datetime.now(tz=timezone.utc), onupdate=datetime.now(tz=timezone.utc))
    address = relationship(
        "Address", back_populates="user", cascade="all, delete, delete-orphan"
    )

    class Config:
        arbitrary_types_allowed = True


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="address")
