#!/usr/bin/python
'''
Driver for the Lynxmotion BotBoarduino
'''

from smbus2 import SMBus
import struct
import time

class BOTBOARDUINO:
    def __init__(self, i2c_bus=1, addr=0x40):
        self.bus = SMBus(i2c_bus);
        self.addr = addr