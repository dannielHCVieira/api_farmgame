from pymongo.mongo_client import MongoClient
import motor.motor_asyncio

uri = "mongodb+srv://dannielvieira:fmMwdlEpxErKdjGV@cluster0.naohgbb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = motor.motor_asyncio.AsyncIOMotorClient(uri)
db = client.unity_farmgame

config_c = db.get_collection("config")
gamedata_c = db.get_collection("game_data")