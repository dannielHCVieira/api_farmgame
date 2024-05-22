from fastapi import APIRouter

from models.request import PlayerdataModel
from helpers.db_connection import playerdata_c

router = APIRouter()

@router.post("/save",
            response_model=PlayerdataModel,
            response_model_by_alias=False)
async def save_data(
    parameters: PlayerdataModel,
):
    response: dict = None

    try:
        print("Saving data!")
        new_log = await playerdata_c.insert_one(parameters.model_dump(by_alias=True, exclude=["id"]))
        print("Data saved! Checking if successful...")
        response = await playerdata_c.find_one(new_log.inserted_id)  
        print("Data saved successfully!")
    except Exception as e:
        response = {"error": str(e)}

    return response

@router.get("/get/{id}",
            response_model=PlayerdataModel,
            response_model_by_alias=False)
async def get_data(
    id: str
):
    response: PlayerdataModel = None

    try:
        response = await playerdata_c.find_one({"criancaUUID": id})
    except Exception as e:
        response = {"error": str(e)}

    return response.model_dump(by_alias=True, exclude=["id"])
