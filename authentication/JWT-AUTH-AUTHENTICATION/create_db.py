from app.config.base import Base
from app.config.db_config import engine
from app.models.user import User

Base.metadata.create_all(engine)