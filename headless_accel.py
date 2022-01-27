# Headless Accelerometer

# Written by Cole Lyman

# 11.30.2021

#import important libraries
import time

import random

from random import randint

import Adafruit_LSM303
import Adafruit_SSD1306

import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#defining pins and accelerometer/LCD
lsm303 = Adafruit_LSM303.LSM303()

RST = 24

DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

#init for display
disp.begin()

disp.clear()
disp.display()

#setting parameters for the image
width = disp.width
height = disp.height
image = Image.new('1', (width,height))

draw = ImageDraw.Draw(image)

font = ImageFont.load_default()
x = 80
y = 25

#failed experiment :(
collision = False

randx = randint(0, width-10)
randy = randint(0, height-10)

points = 0

while True:
  
  #all of this is very similar to the I2C assignment
  disp.clear()

  draw.rectangle((0,0,width,height), outline=0, fill=0)

  accel, mag = lsm303.read()
  accel_x, accel_y, accel_z = accel
  draw.text((2, 2), "X: " + str(round(accel_x*.01 ,2)), font=font, fill=255)
  draw.text((2, 10), "Y: " + str(round(accel_y*.01,2)), font=font, fill=255)
  #draw.text((2, 54), "Points: " +str(points), font=font, fill=255)

  #more failed collision tests
  if x+15 >= randx & x+15 <= randx+10 & y+15 >= randy & y+15 <= randy+10:
    collision = True

  if collision:
    randx = randint(0, width-10)
    randy = randint(0, height-10)
    points +=1

  #draw.ellipse((randx,randy,randx+10,randy+10),outline=255, fill=0)

  y += round(accel_x*.01)
  
  #make sure circle doesn't go off the screen
  if y > height-15:
    y = height-15
  if y < 0:
    y = 0

  x += round(accel_y*.01)

  if x > width - 15:
    x = width - 15
  if x < 0:
    x = 0
    
  #actual drawing of circle
  draw.ellipse((x, y, x+15, y+15), outline=255, fill=0)

  disp.image(image)

  print(x)
  print(y)
  disp.display()
  time.sleep(.01)

