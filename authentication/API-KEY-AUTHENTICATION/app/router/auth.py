from fastapi import APIRouter
from app.views.auth import create_user, create_api_key

auth_router = APIRouter(prefix='/auth')

auth_router.add_api_route("/register", methods=["POST"], endpoint=create_user)
auth_router.add_api_route("/generate-apikey", methods=["POST"], endpoint=create_api_key)