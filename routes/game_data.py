from fastapi import APIRouter

from models.request import GamedataModel
from helpers.db_connection import gamedata_c

router = APIRouter()

@router.get("/health")
async def healthcheck():
    return {"status": "OK"}

@router.post("/log",
            response_model=GamedataModel,
            response_model_by_alias=False)
async def log_data(
    parameters: GamedataModel,
):
    response: dict = None

    try:
        print("Saving data!")
        new_log = await gamedata_c.insert_one(parameters.model_dump(by_alias=True, exclude=["id"]))
        print("Data saved! Checking if successful...")
        response = await gamedata_c.find_one(new_log.inserted_id)  
        print("Data saved successfully!")
    except Exception as e:
        response = {"error": str(e)}

    return response

@router.get("/get/{id}",
            response_model=GamedataModel,
            response_model_by_alias=False)
async def get_data(
    id: str
):
    response: GamedataModel = None

    try:
        response = await gamedata_c.find_one({"criancaUUID": id})
    except Exception as e:
        response = {"error": str(e)}

    return response.model_dump(by_alias=True, exclude=["id"])
