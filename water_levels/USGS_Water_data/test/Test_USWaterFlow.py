# -*- UTF-8 -*-
"""
Script created for the Iceye assessment.
@author: Yonatan Shahar
"""

from USGS_Water_data.Us_Water_flow import get_usgs_data

# Test the retrival of data from the USGS data center.
def test_retrival_data():
    site_number = "02176930"
    start_date = "2022-10-01"
    end_date = "2023-09-30"

    test_data = get_usgs_data(site_number, start_date, end_date)
    assert test_data[0].get("00060").iloc[0] == 56.5
