from fastapi import APIRouter

from models.request import GamedataRequest

router = APIRouter()

@router.get("/health")
async def healthcheck():
    return {"status": "OK"}

@router.post("/log")
async def log_data(
    parameters: GamedataRequest,
):
    response: dict = None



    response = {
        "status": "GameData logged!"
    }
    return response