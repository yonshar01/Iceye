# -*- UTF-8 -*-
"""
Script created for the Iceye assessment.
@author: Yonatan Shahar
"""

from USGS_Water_data.Us_Water_flow import get_usgs_data

from Utility.constants import usgs_water_stations

startDate = "2023-10-01"
endDate = "2023-10-02"

# Insert the data of the station listed in usgs_water_stations
for station in usgs_water_stations:
    print(station)
    get_usgs_data(station, startDate, endDate)
