from fastapi import Security, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from app.dependencies.session import get_db
from sqlalchemy.orm import Session
from app.models.auth import APIKey

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


def validate_api_key(api_key_header: str = Security(api_key_header), db: Session = Depends(get_db)):
    if api_key_header is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Please provide an API Key"
        )

    api_key = db.query(APIKey).filter(APIKey.api_key == api_key_header).first()

    if api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key"
        )
    
    return api_key
