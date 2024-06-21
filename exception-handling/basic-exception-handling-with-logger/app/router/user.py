from fastapi import APIRouter
from app.views.user import retrieve_user, create_user, list_users, update_user, delete_user
from app.serializers.user import RetrieveUserSerializer, ListUserSerializer

router = APIRouter(prefix="/users", tags=["user"])

router.add_api_route("/", methods=["GET"], endpoint=list_users, response_model=ListUserSerializer)
router.add_api_route("/", methods=["POST"], endpoint=create_user, response_model=RetrieveUserSerializer)

router.add_api_route("/{user_id}", methods=["GET"], endpoint=retrieve_user, response_model=RetrieveUserSerializer)
router.add_api_route("/{user_id}", methods=["PUT"], endpoint=update_user, response_model=RetrieveUserSerializer)
router.add_api_route("/{user_id}", methods=["DELETE"], endpoint=delete_user, response_model=RetrieveUserSerializer)