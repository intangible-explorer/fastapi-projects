from fastapi import APIRouter
from app.views.user import list_users

user_router = APIRouter(prefix="/users", tags=["user"])

user_router.add_api_route("/", methods=["GET"], endpoint=list_users)