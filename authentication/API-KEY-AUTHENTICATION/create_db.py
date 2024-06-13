from app.config.base import Base
from app.models.auth import User, APIKey
from app.config.db_config import engine

Base.metadata.create_all(bind=engine)