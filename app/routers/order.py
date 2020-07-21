from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/orders/")
async def create_order():
    pass
