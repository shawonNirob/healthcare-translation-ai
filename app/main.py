from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.healthcare_ai import router as healthcare_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(healthcare_router, prefix="/ai", tags=["healthcare"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Healthcare Translation API"}

@app.get("/_status")
def status():
    return {"status": "ok"}


