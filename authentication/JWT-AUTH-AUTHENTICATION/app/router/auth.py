from fastapi import APIRouter
from app.views.auth import create_user, get_access_token, refresh_token

router = APIRouter(prefix="/auth", tags=["auth"])

router.add_api_route("/register", methods=["POST"], endpoint=create_user)
router.add_api_route("/login", methods=["POST"], endpoint=get_access_token)
router.add_api_route("/refresh-token", methods=["POST"], endpoint=refresh_token)
