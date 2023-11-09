# -*- UTF-8 -*-
"""
Script created for the Iceye assessment.
@author: Yonatan Shahar
"""

import pandas as pd
import constants
import psycopg2


def get_eau_data(station_id):
    """
    Get the data by station id and insert the data into a local postgresql instance. It is not a GIS database left to discuss
    in the future or alternatives to store the data as it is expected a large datasets and a very large number of sites in France.

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

        # Query to get data by station. The %()S is use here to make it clear
        query_getdata = """SELECT * FROM eau_france_water_level.water_level where code_station = %(Station)s ORDER BY id ASC"""

        data = {"Station": station_id}

        cursor.execute(query_getdata, data)

        response_data = cursor.fetchall()

        eau_df = pd.DataFrame(response_data)

        cursor.close()
        connection.close()

        return eau_df

    except psycopg2.DatabaseError as e:
        print(f"Postgres error: {e}")
