import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time

WIDTH = 128
HEIGHT = 64
BORDER = 2

BANNER = ''' 
 __  __      ___ __
|__)/  \\\\  /|__ |__)
|  \\\\__/ \\/ |___|  \\'''.splitlines()

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

    def draw_text(self, text, position, auto = False):
        if auto: self.start_drawing()
        font = ImageFont.load_default()
        (font_width, font_height) = font.getsize(text)
        self.draw.text((position[0]+BORDER, position[1]+BORDER), text, font=font, fill=255)
        if auto: self.show_drawing()
    
    def write(self, lines, auto = False):
        if len(lines) > 6:
                raise ValueError(f"The number of lines provided is exceding a 5 limit.")
        if auto: self.start_drawing()
        max_length = 21
        font = ImageFont.load_default()
        for index, line in enumerate(lines):
            if len(line) > max_length:
                raise ValueError(f"The line {index} is exceding a 21 characters limit.")
            self.draw.text((0+BORDER,(10 * index)+BORDER), line, font=font, fill=255)
        if auto: self.show_drawing()

    def banner_animation(self):
        self.write(BANNER, True)
        time.sleep(1.5)
        empty_space = BANNER
        for i in range(6):
            for j in range(21):
                empty_space[i][j] + ' '
                self.write(empty_space[i][j], True)
                time.sleep(0.25)
        self.clear(True)

    def clear(self, auto = False):
        if auto: self.start_drawing()
        self.oled.fill(0)
        if auto: self.show_drawing()

    def show_drawing(self):
        self.oled.image(self.image)
        self.oled.show()