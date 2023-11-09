from GetWaterLevels import insert_data

from Utility.constants import eau_france_stations

for station in eau_france_stations:
    print(station)
    insert_data(station)
