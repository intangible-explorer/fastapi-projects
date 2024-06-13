from fastapi import APIRouter
from app.views.public import test_public

public_router = APIRouter(prefix='/public')

public_router.add_api_route("/test", methods=["GET"], endpoint=test_public)