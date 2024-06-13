from fastapi import APIRouter
from app.views.authentication import register_user
authentication_router = APIRouter(prefix="/auth", tags=["user"])

authentication_router.add_api_route("/register", methods=["POST"], endpoint=register_user)

