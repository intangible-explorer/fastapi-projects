from fastapi import Depends, HTTPException, status
from app.utils.jwt import decode_token
from fastapi.security import OAuth2PasswordBearer
from app.dependencies.session import db_dependency
from app.models.user import User
from typing import Annotated
from app.serializers.user import RetrieveUserSerializer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_user(db, username: str):
    user = db.query(User).filter(User.username == username).first()
    return user

async def get_current_user(db: db_dependency, token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access token is either expired or invalid. Please check",
            headers={"WWW-Authenticate": "Bearer"},
        )
    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = get_user(db, username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# dependency
get_current_user_dependency = Annotated[RetrieveUserSerializer, Depends(get_current_user)]