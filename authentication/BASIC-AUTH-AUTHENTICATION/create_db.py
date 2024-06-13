from app.config.base import Base
from app.config.db_config import engine
from app.models import *

Base.metadata.create_all(bind=engine)