import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

WIDTH = 128
HEIGHT = 64
BORDER = 5

import adafruit_ssd1306

class SSD1306:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, self.i2c, addr=0x3c)
        
        self.image = None
        self.draw = None

    def start_drawing(self):
        self.image = Image.new('1', (self.oled.width, self.oled.height))
        self.draw = ImageDraw.Draw(self.image)

    def draw_text(self, text, position):
        font = ImageFont.load_default()
        (font_width, font_height) = font.getsize(text)
        self.draw.text(position, text, font=font, fill=255)

    def show_drawing(self):
        self.oled.image(self.image)
        self.oled.show()