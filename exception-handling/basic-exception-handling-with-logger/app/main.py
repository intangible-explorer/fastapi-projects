from fastapi import FastAPI, Request
from app.router import user
from app.exceptions import CustomAPIException
from fastapi.responses import JSONResponse
from app.config.logger_config import logger

app = FastAPI()

app.include_router(user.router)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response

@app.get("/")
async def root():
    return {"message": "From FastAPI!"}
