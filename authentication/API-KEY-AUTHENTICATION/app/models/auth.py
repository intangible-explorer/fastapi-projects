from app.config.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String) 
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True)
    api_key = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))
