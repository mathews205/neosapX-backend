from fastapi import APIRouter

router = APIRouter(prefix="/shops", tags=["Shops"])


@router.get("/ping")
def ping_shops():
    return {"message": "shops router working"}