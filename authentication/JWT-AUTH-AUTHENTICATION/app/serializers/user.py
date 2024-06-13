from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

    class Config:
        from_attributes=True

class CreateUserSerializer(UserBase):
    password: str

class RetrieveUserSerializer(UserBase):
    id: int

    class Config:
        from_attributes=True
