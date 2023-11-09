import time

from Utility.process import processing

count = 0
while count < 2:
    print(count)
    processing("periodic_insert.py")
    count += 1
    time.sleep(5)
