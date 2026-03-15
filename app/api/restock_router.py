from fastapi import APIRouter

router = APIRouter(prefix="/restock-requests", tags=["Restock Requests"])


@router.get("/ping")
def ping_restock():
    return {"message": "restock router working"}