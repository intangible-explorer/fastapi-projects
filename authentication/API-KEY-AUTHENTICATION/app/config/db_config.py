from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.settings import get_settings

settings = get_settings()

'''Create Engine'''
engine = create_engine(settings.DATABASE_URL)

'''Create Session'''
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
