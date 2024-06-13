from typing import Annotated
from fastapi import HTTPException, status, Depends, Body
from fastapi.security import OAuth2PasswordRequestForm
from app.dependencies.session import db_dependency
from app.serializers.user import CreateUserSerializer
from app.models.user import User
from app.utils.auth import hash_password
from app.utils.jwt import create_access_token, create_refresh_token, decode_token
from app.utils.user import authenticate_user
from app.config.settings import get_settings
from app.serializers.auth import TokenSerializer

settings = get_settings()

def create_user(user: CreateUserSerializer, db: db_dependency):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User with username: {user.username}, already exists")

    new_user = User(username=user.username, hashed_password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}


def get_access_token(db: db_dependency, form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    # create access token
    data = {"sub": user.username, "id": user.id}
    access_token = create_access_token(data)
    refresh_token = create_refresh_token(data)
    return TokenSerializer(access_token=access_token, token_type="bearer", refresh_token=refresh_token)


def refresh_token(db: db_dependency, body: dict = Body(...)):
    refresh_token = body.get("refresh_token")
    payload = decode_token(refresh_token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    username = payload.get("sub")
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    data = {"sub": user.username, "id": user.id}
    access_token = create_access_token(data)
    return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}