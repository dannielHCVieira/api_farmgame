from fastapi import APIRouter

from models.request import GamedataRequest
from helpers.db_connection import gamedata_c

router = APIRouter()

@router.get("/health")
async def healthcheck():
    return {"status": "OK"}

@router.post("/log")
async def log_data(
    parameters: GamedataRequest,
):
    response: dict = None

    new_log = await gamedata_c.insert_one(parameters.model_dump())
    
    response = await gamedata_c.find_one(
        {"criancaUUID": new_log.criancaUUID,
         "especialistaId": new_log.especialistaId,
         "jogoId": new_log.jogoId}
    )

    return response