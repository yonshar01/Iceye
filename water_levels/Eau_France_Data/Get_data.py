import pandas as pd
import constants
import psycopg2


def get_eau_data(station_id):
    try:
        connection = psycopg2.connect(
            database=constants.database,
            host=constants.host,
            user=constants.user,
            password=constants.password,
        )
        cursor = connection.cursor()

        query_getdata = """SELECT * FROM eau_france_water_level.water_level where code_station = %(Station)s ORDER BY id ASC"""

        data = {"Station": station_id}

        cursor.execute(query_getdata, data)

        response_data = cursor.fetchall()

        eau_df = pd.DataFrame(response_data)

        return eau_df

    except psycopg2.DatabaseError as e:
        print(f"Postgres error: {e}")

    finally:
        if connection:
            connection.close()
        cursor.close()
