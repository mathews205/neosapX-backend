from fastapi import APIRouter

router = APIRouter(prefix="/expiry-batches", tags=["Expiry Batches"])


@router.get("/ping")
def ping_expiry():
    return {"message": "expiry router working"}