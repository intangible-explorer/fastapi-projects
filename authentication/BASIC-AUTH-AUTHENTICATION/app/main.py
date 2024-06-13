from fastapi import FastAPI
from app.router.authentication import authentication_router
from app.router.user import user_router

app = FastAPI()

# include routers
app.include_router(authentication_router)
app.include_router(user_router)

# unprotected route
@app.get("/")
async def read_root():
    return {"Hello": "World"}