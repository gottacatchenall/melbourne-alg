#! /usr/bin/env python

import Adafruit_DHT
import datetime
import time
import numpy as np

# ==============================================
# Run Setup
# ==============================================

runname = "RUN"
sleeptime = 1
totalruntime = 10

# ==============================================
# End Run Setup
# ==============================================

sensor = Adafruit_DHT.DHT22
pin = 23

starttime = time.time()

t = []
h = []

timeout = time.time() + totalruntime

while True:
    t_now = time.time() - starttime
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    t.append(t_now)
    h.append(humidity)
    time.sleep(sleeptime)

    if (time.time() > timeout):
        break

data = np.zeros((2, len(t)))

data[0,:] = t
data[1,:] = h

np.savetxt(runname + ".csv", data, fmt='%10.2f', delimiter=",")

