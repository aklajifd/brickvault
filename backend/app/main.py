from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.routers import themes, sets, collection

app = FastAPI(
    title=settings.app_name,
    description="LEGO collection tracker",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(themes.router)
app.include_router(sets.router)
app.include_router(collection.router)

@app.get("/health")
async def health_check():
    return {"status": "ok", "app": settings.app_name}