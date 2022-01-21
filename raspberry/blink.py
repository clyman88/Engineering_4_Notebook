import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BCM)

<<<<<<< HEAD
channel_list = [5, 12, 20]
=======
channel_list = [5, 12, 21]
>>>>>>> 48b66eec9b7ae6d5c5de3174a26169d71162fb5f

GPIO.setup(channel_list, GPIO.OUT, initial=GPIO.LOW)

def solo(lis, a, b):
	for i in lis:
		if i !=a:
			GPIO.output(i, False)
		else:
			GPIO.output(i, True)
	sleep(b)

while True:
	for i in channel_list:
		solo(channel_list, i, .25)
