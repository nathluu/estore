from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/login")
async def login():
    return {"message": "hello world!"}


@router.post("/logout")
async def logout():
    pass
