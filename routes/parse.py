from fastapi import APIRouter

router = APIRouter()

@router.get("/parse/ping")
def ping():
    return {"msg": "parse route ok"}
