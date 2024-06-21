from app.config.base import Base
from app.models.user import User
from app.config.db_config import engine

Base.metadata.create_all(bind=engine)