# RPi GPIO Pin Introduction

# Written by Cole Lyman

# 11.18.2021

# import important thangs
import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BCM)

#list of LED pins
channel_list = [5, 12, 21]

GPIO.setup(channel_list, GPIO.OUT, initial=GPIO.LOW)

#function for turning on ONLY one LED
def solo(lis, a, b):
	for i in lis:
		if i !=a:
			GPIO.output(i, False)
		else:
			GPIO.output(i, True)
	sleep(b)

#keep running above function, switching LEDs in the list initially defined
while True:
	for i in channel_list:
		solo(channel_list, i, .25)
