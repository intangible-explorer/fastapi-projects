from sqlalchemy import create_engine
from app.config.settings import get_settings
from sqlalchemy.orm import sessionmaker

settings = get_settings()

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)