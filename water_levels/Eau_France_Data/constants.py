# -*- UTF-8 -*-
"""
Script created for the Iceye assessment.
@author: Yonatan Shahar
"""

# This DB access credentials are here use ina unsafe manner. In a commercial setting this
# must be kept in a secure way such as AWS secrets
database = "WaterLevel"
host = "localhost"
user = "postgres"
password = "Habonim1998$"
port = 5432

json_file_name = 'response.json'

# the sites to run the processes
eau_france_stations = ["F490000104", "F664000404", "F700000103"]
usgs_water_stations = ["03443000", "03441000", "03441440"]
