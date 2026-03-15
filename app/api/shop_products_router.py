from fastapi import APIRouter

router = APIRouter(prefix="/shop-products", tags=["Shop Products"])


@router.get("/ping")
def ping_shop_products():
    return {"message": "shop products router working"}