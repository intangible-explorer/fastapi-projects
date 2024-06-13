from app.config.db_config import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# dependency
db_dependency = Annotated[Session, Depends(get_db)]