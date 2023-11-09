# -*- UTF-8 -*-
"""
Script created for the Iceye assessment.
@author: Yonatan Shahar
"""

from Get_EauFrance_WaterLevels import insert_data

from Utility.constants import eau_france_stations

# This script simply insert the data
for station in eau_france_stations:
    print(station)
    insert_data(station)
