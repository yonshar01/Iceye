# -*- UTF-8 -*-
"""
Script created for the Iceye assessment.
@author: Yonatan Shahar 
"""

import json
import psycopg2
import requests

# local
from Utility import constants


def get_water_levels(station_id):
    """
    Get the last 1000 recordings from the Aau France API.
    :param station_id:
    :return: The returned data
    """

    # The service end point
    url = "https://hubeau.eaufrance.fr/api/v1/hydrometrie/observations_tr?code_entite={std_id}".format(
        std_id=station_id,
    )

    # Get the available data
    samples_number = json.loads(requests.get(url).text)["count"]

    # If there are data in the response
    if samples_number > 0:
        url = (
            "https://hubeau.eaufrance.fr/api/v1/hydrometrie/observations_tr?code_entite={std_id}&size={sam_num}&grandeur_hydro=H&"
        ).format(std_id=station_id, sam_num=1000)

        response_api = requests.get(url)

        response_code = response_api.status_code

        water_level_data = json.loads(response_api.text)

    else:
        # custom exception, it needs to add all the possible exceptions throw
        raise Exception("No Station with valid data found")

    return response_code, water_level_data


def insert_data(station_id):
    """
    Insert the data into a local postgresql database
    :param station_id:
    :return:
    """
    try:
        connection = psycopg2.connect(
            database=constants.database,
            host=constants.host,
            user=constants.user,
            password=constants.password,
        )

        cursor = connection.cursor()

        data_insert = get_water_levels(station_id)[1]["data"]

        # For loop to interact through received data.
        for item in data_insert:
            # Variables to insert the relevant data
            code_station = item["code_station"]
            date_start = item["date_debut_serie"]
            date_end = item["date_fin_serie"]
            obs_date = item["date_obs"]
            obs_result = item["resultat_obs"]
            longitude = item["longitude"]
            latitude = item["latitude"]

            # Formatted query
            insert_query = (
                "insert into eau_france_water_level.water_level(code_station, date_start_serie, date_end_serie, obs_date, obs_result, longitude, latitude) "
                "values(%(Code_Station)s,%(Date_start)s, %(Date_end)s, %(Obs_date)s, %(Obs_results)s, %(Long)s, %(Lat)s)"
            )

            data = {
                "Code_Station": code_station,
                "Obs_date": obs_date,
                "Date_start": date_start,
                "Date_end": date_end,
                "Obs_results": obs_result,
                "Long": longitude,
                "Lat": latitude,
            }

            cursor.execute(insert_query, data)

            connection.commit()

        cursor.close()
        connection.close()

    except psycopg2.DatabaseError as e:
        print(f"Progres error: {e}")
