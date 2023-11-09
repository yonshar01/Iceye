import dataretrieval.nwis as nwis
import psycopg2
from sqlalchemy import create_engine

from Utility import constants

# Set the parameters needed to retrieve data
siteNumber = "03443000"
startDate = "2023-10-01"
endDate = "2023-10-02"


# Retrieve the data
def get_usgs_data(site, start_date, end_date):
    conn_string = f"postgresql://{constants.user}:{constants.password}@{constants.host}:{constants.port}/{constants.database}"

    db = create_engine(conn_string)
    connection = db.connect()

    daily_streamflow = nwis.get_iv(sites=site, start=start_date, end=end_date)

    # Prepare the dataset to be inserted into the database. If it needs to be added to the change replace for append
    daily_streamflow[0].to_sql(
        "usgs_data", con=connection, schema="USGS data", if_exists="append", index=True
    )

    conn = psycopg2.connect(conn_string)
    conn.autocommit = True

    connection.close()

    return daily_streamflow
