import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i2c = busio.I2C(board.SCL, board.SDA)

WIDTH = 128
HEIGHT = 64
BORDER = 5

import adafruit_ssd1306
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3c)

oled.fill(1)
oled.show()