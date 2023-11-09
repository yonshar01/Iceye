import json
import shutil
from fastapi import FastAPI
from fastapi import UploadFile
from fastapi.responses import FileResponse
from pathlib import Path

from Get_data import get_eau_data
from constants import eau_france_stations

# PS D:\Iceye\water_levels> uvicorn testing_FastAPI:app --reload
app = FastAPI()


@app.get("/users")
async def read_users():
    output = get_eau_data(eau_france_stations[0])

    output.info()

    output.to_json("response.json", orient="index", date_format="iso")

    return FileResponse("response.json", media_type="json", filename="response.json")
