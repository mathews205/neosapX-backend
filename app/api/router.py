from fastapi import APIRouter

from app.api.shops_router import router as shops_router
from app.api.products_router import router as products_router
from app.api.categories_router import router as categories_router
from app.api.shop_products_router import router as shop_products_router
from app.api.restock_router import router as restock_router
from app.api.expiry_router import router as expiry_router

api_router = APIRouter()

api_router.include_router(shops_router, prefix="/shops", tags=["Shops"])
api_router.include_router(products_router, prefix="/products", tags=["Products"])
api_router.include_router(categories_router, prefix="/categories", tags=["Categories"])
api_router.include_router(shop_products_router, prefix="/shop-products", tags=["Shop Products"])
api_router.include_router(restock_router, prefix="/restock", tags=["Restock"])
api_router.include_router(expiry_router, prefix="/expiry", tags=["Expiry"])