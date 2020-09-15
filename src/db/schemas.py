from typing import List
from pydantic import BaseModel


class AddressBase(BaseModel):
    email_address: str


class AddressCreate(AddressBase):
    pass


class Address(AddressBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserBase(BaseModel):
    name: str
    fullname: str
    nickname: str

    class Config:
        arbitrary_types_allowed = True


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    address: List[Address] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
