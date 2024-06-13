from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class CreateUser(UserBase):
    password: str
