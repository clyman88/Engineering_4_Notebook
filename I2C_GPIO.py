# RPi GPIO Pins - I2C

# Written by Cole Lyman

# 11.30.2021

# import libraries
import time

import Adafruit_LSM303
import Adafruit_SSD1306

import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#defining the accelerometer
lsm303 = Adafruit_LSM303.LSM303()

RST = 24

DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

#defining the LCD
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

#necessary commands to begin displaying text/objects on screen
disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height

#"Image" is the surface on which we'll be drawing
image = Image.new('1', (width,height))

draw = ImageDraw.Draw(image)

#font!
font = ImageFont.load_default()

while True:

  disp.clear()
  
  #IMPORTANT. This rectangle "clears" the screen. Include this line.
  draw.rectangle((0,0,width,height), outline=0, fill=0)
  
  #accel is defined as a tuple, I believe, and each value is assigned to x, y, and z
  accel, mag = lsm303.read()
  accel_x, accel_y, accel_z = accel
  
  #display text with accelerometer output
  draw.text((2, 2), "X: " + str(round(accel_x*.01 ,2)), font=font, fill=255)
  draw.text((2, 10), "Y: " + str(round(accel_y*.01,2)), font=font, fill=255)
  draw.text((2, 18), "Z: " + str(round(accel_z*.01,2)), font=font, fill=255)
  
  disp.image(image)

  disp.display()
  time.sleep(.2)
 
