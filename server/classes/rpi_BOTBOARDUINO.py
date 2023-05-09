#!/usr/bin/python
'''
Driver for the Lynxmotion BotBoarduino
'''

from smbus2 import SMBus
import struct
import time

class BOTBOARDUINO:
    def __init__(self, i2c_bus=1, addr=0x40, register=0):
        try:
            self.bus = SMBus(i2c_bus)
            self.addr = addr
            self.addr = register
        except:
            print('Unable to initialize i2c connection')

    def send(self, data):
        try:
            self.bus.write_i2c_block_data(self.addr, self.register, data)
        except:
            print(data)