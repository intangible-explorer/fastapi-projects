from app.dependencies.session import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, Body, HTTPException
from app.models import User
from app.serializers.user import CreateUser

def register_user(credentials: CreateUser = Body(...), db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == credentials.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail=f"user with email: {credentials.email} already exists")

    new_user = User(email=credentials.email, password=credentials.password)
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}


