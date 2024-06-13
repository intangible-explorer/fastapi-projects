from fastapi import FastAPI
from app.router import auth, protected

app = FastAPI()

app.include_router(auth.router)
app.include_router(protected.router)

@app.get("/")
def root():
    return {"message": "World"}