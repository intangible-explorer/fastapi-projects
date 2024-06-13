from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: str 
    last_name: str
    email: str

    class Config:
        from_attributes=True

class CreateUserSerializer(UserBase):
    password: str

class RetrieveUserSerializer(UserBase):
    id: int

    class Config:
        from_attributes=True