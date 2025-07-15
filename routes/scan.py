from fastapi import APIRouter

router = APIRouter()

@router.get("/scan/ping")
def ping():
    return {"msg": "scan route ok"}
