from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/ping")
def ping_products():
    return {"message": "products router working"}