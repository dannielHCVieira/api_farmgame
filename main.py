from typing import Optional
from fastapi import FastAPI

from routes.game_data import router as game_data_router
from routes.player_data import router as player_data_router

app = FastAPI(
    title="FarmGame API",
    description="API for logging Farm game data",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router=game_data_router, prefix="/v1/gamedata", tags=["gamedata"])

app.include_router(router=player_data_router, prefix="/v1/playerdata", tags=["playerdata"])
