import time
import smbus
import json

class ESP32:
    def __init__(self):
        self.address = 0x08
        self.i2c = smbus.SMBus(1)
        self.received_data = ""

    def getData(self):
        received_data = self.i2c.read_i2c_block_data(self.address, 0, 11)
        for i in range(len(received_data)):
            self.received_data += chr(received_data[i])
        data_to_submit = self.received_data
        received_data = None
        self.received_data = ""
        return data_to_submit