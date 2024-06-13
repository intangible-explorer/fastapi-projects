from app.dependencies.session import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from app.models import User
from app.dependencies.user import get_current_user

def list_users(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    print("current logged in user:", current_user)
    return {"message": "success"}