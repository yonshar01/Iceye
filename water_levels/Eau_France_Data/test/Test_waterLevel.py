# -*- UTF-8 -*-
"""
Script created for the Iceye assessment.
@author: Yonatan Shahar
"""

from pytest import raises

from Eau_France_Data.Get_EauFrance_WaterLevels import get_water_levels
from Eau_France_Data.periodic_insert import insert_data


class TestWaterLevels:
    """
    Class  to run the test. They are a very simple and needs to be more test cases for better coverage at the moment is 95%
    """

    def test_get_water_levels(self):
        test_data = get_water_levels("Y251002001")

        assert test_data[0] == 206
        assert test_data[1]["count"] > 1

    def test_exception_water_levels(self):
        with raises(Exception):
            test_data = get_water_levels("Y251009987564")
