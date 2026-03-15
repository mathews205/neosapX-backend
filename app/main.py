from fastapi import FastAPI

from app.api.shops_router import router as shops_router
from app.api.products_router import router as products_router
from app.api.shop_products_router import router as shop_products_router
from app.api.restock_router import router as restock_router
from app.api.expiry_router import router as expiry_router

app = FastAPI(title="NeoSapX API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "NeoSapX API is running"}


app.include_router(shops_router)
app.include_router(products_router)
app.include_router(shop_products_router)
app.include_router(restock_router)
app.include_router(expiry_router)