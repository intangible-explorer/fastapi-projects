from fastapi import APIRouter
from app.views.protected import test_protected

protected_router = APIRouter(prefix='/protected')

protected_router.add_api_route("/test", methods=["GET"], endpoint=test_protected)