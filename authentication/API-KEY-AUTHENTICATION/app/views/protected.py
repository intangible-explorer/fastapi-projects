from app.dependencies.auth import validate_api_key
from fastapi import Depends
# from fastapi.security import API

def test_protected(api_key: str = Depends(validate_api_key)):
    return {"message": "Procted route accessed with APIKey"}