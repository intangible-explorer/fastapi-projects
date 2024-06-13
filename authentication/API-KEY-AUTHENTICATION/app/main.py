from fastapi import FastAPI
from app.router import public, auth, protected

app = FastAPI()

app.include_router(public.public_router)
app.include_router(auth.auth_router)
app.include_router(protected.protected_router)

@app.get("/")
def root():
    return {"message": "hey world!"}