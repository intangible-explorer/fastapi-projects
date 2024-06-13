from app.config.db_config import SessionLocal

'''Dependency to get DB session'''
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()