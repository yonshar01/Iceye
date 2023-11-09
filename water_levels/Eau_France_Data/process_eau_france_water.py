# -*- UTF-8 -*-
"""
Script created for the Iceye assessment.
@author: Yonatan Shahar
"""

import time

from Utility.process import processing

count = 0
# This script run processing a instance of subprocess. Here run a while until the count reach two.
# it can use a scheduler or use time. It runs the script every 5 secs.
while count < 2:
    print(count)
    processing("periodic_insert.py")
    count += 1
    time.sleep(5)
