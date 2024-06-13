from app.dependencies.session import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, Body
from app.serializers.auth import CreateUserSerializer, RetrieveUserSerializer
from app.models.auth import User, APIKey
import secrets


def create_user(credentials: CreateUserSerializer = Body(...), db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == credentials.email).first()
    if existing_user:
        raise Exception("User already exists")
    user = User(**credentials.__dict__)
    db.add(user)
    db.commit()
    db.refresh(user)
    return RetrieveUserSerializer.model_validate(user)

def create_api_key(user_id: int, db: Session = Depends(get_db)):
    key = secrets.token_urlsafe(32)
    api_key = APIKey(api_key=key, user_id=user_id)
    db.add(api_key)
    db.commit()
    db.refresh(api_key)
    return {"API_KEY": api_key.api_key}