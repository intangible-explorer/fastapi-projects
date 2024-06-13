from fastapi import APIRouter
from app.views.protected import test

router = APIRouter(prefix="/protected", tags=["protected"])

router.add_api_route("/test", methods=["GET"] ,endpoint=test)