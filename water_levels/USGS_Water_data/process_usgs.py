import time

from Utility.process import processing

count = 0
while count < 2:
    print(count)
    processing("USGS_periodic.py")
    count += 1
    time.sleep(5)