
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from generator import Generator

api = FastAPI()
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)
models = {
    "Quotes": Generator("Quotes"),
    "Shakespeare": Generator("Shakespeare"),
    "Whatsapp": Generator("Whatsapp"),
    "News": Generator("News"),
}


@api.get("/")
async def root():
    return "For more info, go to /docs"


@api.get("/get/{model}")
async def get_model(model: str):
    """Returns a generated sentence using specified model"""
    if model in models:
        return models[model].get()
    else:
        return {"error": "Model not found"}


@api.get("/list_models")
async def list_model():
    """Lists all available models"""
    return {"models": list(models.keys())}
