from app.models.user import User
from app.utils.auth import verify_password
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

def authenticate_user(db: Session, form_data: OAuth2PasswordRequestForm):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user:
        return False
    if not verify_password(form_data.password, user.hashed_password):
        return False
    return user