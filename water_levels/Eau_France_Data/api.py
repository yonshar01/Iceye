# -*- UTF-8 -*-
"""
Script created for the Iceye assessment.
@author: Yonatan Shahar
"""
from fastapi import FastAPI
from fastapi.responses import FileResponse

import constants
from Get_data import get_eau_data
from constants import eau_france_stations

app = FastAPI()

# To run this api: uvicorn api:app --reload

# API end point
@app.get("/download")
async def download_file():
    """
    This simple FastApi is used to pull data from the database, saved to a json file and make it available to download
    at the end point /download
    :return: a FileRespond
    """
    output = get_eau_data(eau_france_stations[0])

    output.to_json(constants.json_file_name, orient="index", date_format="iso")

    return FileResponse(constants.json_file_name, media_type="json", filename=constants.json_file_name)
