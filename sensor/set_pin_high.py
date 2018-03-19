#! /usr/bin/env python

import RPi.GPIO as GPIO
import time

pin_num = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_num, GPIO.OUT)

print 'settig hi!'
GPIO.output(pin_num, GPIO.HIGH)
time.sleep(5)
print 'setting lo!'
GPIO.output(pin_num, GPIO.LOW)

