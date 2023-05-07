#!/usr/bin/python
'''
Driver for the Lynxmotion BotBoarduino
'''

from smbus2 import SMBus
import struct
import time

class BOTBOARDUINO:
    def __init__(self, i2c_bus=1, addr=0x40, register=0):
        self.bus = SMBus(i2c_bus)
        self.addr = addr
        self.addr = register

    def send(self, data):
        self.bus.write_i2c_block_data(self.addr, self.register, data)