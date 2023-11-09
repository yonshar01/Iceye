from USGS_Water_data.Us_Water_flow import get_usgs_data

from Utility.constants import usgs_water_stations

startDate = "2023-10-01"
endDate = "2023-10-02"

for station in usgs_water_stations:
    print(station)
    get_usgs_data(station, startDate, endDate)
