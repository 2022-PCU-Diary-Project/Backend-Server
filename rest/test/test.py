from fastapi import APIRouter

router = APIRouter()


@router.get("/message", tags=["get"])
async def test():
    return {"Message": "Test Message!"}
