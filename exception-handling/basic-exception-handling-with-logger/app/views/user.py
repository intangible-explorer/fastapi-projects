from app.dependencies.session import db_dependency
from app.models.user import User
from fastapi import HTTPException
from app.serializers.user import CreateUserSerializer, UpdateUserSerializer, RetrieveUserSerializer
from app.config.logger_config import logger


def list_users(db: db_dependency):
    users = db.query(User).all()
    return {"users": users}

def create_user(db: db_dependency, user: CreateUserSerializer):
    try:
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")
        user = User(**user.__dict__)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except HTTPException as e:
        logger.error(str(e))
        db.rollback()
        raise e
    except Exception as e:
        logger.error(str(e))
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def retrieve_user(db: db_dependency, user_id: int):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except HTTPException as e:
        logger.error(str(e))
        db.rollback()
        raise e
    except Exception as e:
        logger.error(str(e))
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def update_user(db: db_dependency, user_id: int, user_update: UpdateUserSerializer):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        for key, value in user_update.__dict__.items():
            if value is not None:
                setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user
    except HTTPException as e:
        logger.error(str(e))
        db.rollback()
        raise e
    except Exception as e:
        logger.error(str(e))
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def delete_user(db: db_dependency, user_id: int):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        db.delete(user)
        db.commit()
        return {"message": "User deleted successfully"}
    except HTTPException as e:
        logger.error(str(e))
        db.rollback()
        raise e
    except Exception as e:
        logger.error(str(e))
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))