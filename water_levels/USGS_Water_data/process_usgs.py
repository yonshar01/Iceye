# -*- UTF-8 -*-
"""
Script created for the Iceye assessment.
@author: Yonatan Shahar
"""

import time

from Utility.process import processing

# Runs the USGS periodic script to insert the data in the list of sites
count = 0
# Runs until count reach two. It can be run in a scheduler instance
while count < 2:
    print(count)
    processing("USGS_periodic.py")
    count += 1
    time.sleep(5)
