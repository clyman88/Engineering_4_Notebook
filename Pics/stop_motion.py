import time
import picamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pin = 26
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

toggle = False

num = 1

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    time.sleep(2)
    print("Ready!")
    while True:
        if GPIO.input(pin) == False and not toggle:
            toggle = True
            camera.capture("Stop-Motion/pic" + str(num) + ".jpg")
            print("Picture taken ("+str(num)+").")
            num += 1
        elif GPIO.input(pin) == True:
            toggle = False

