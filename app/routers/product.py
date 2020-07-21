from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/products/")
async def get_products():
    pass


@router.get("/products/{product_id}")
async def get_product(product_id: int):
    pass


@router.post("/products/")
async def create_product():
    pass
