from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class CreateUserSerializer(UserBase):
    pass

class RetrieveUserSerializer(UserBase):
    id: int
    created_at:  datetime
    updated_at: datetime

class ListUserSerializer(BaseModel):
    users: List[RetrieveUserSerializer]

class UpdateUserSerializer(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]