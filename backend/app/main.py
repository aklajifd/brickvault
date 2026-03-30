from fastapi import FastAPI

app = FastAPI(
    title="BrickVault API",
    description="LEGO collection tracker",
    version="0.1.0",
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}