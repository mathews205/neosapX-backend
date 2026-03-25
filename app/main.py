from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="NeoSapX API",
    version="0.1.0",
    description="Retail Operations Automation Backend for small convenience stores",
)


@app.get("/", tags=["Health"])
def root():
    return {"message": "NeoSapX API running"}


app.include_router(api_router, prefix="/api/v1")