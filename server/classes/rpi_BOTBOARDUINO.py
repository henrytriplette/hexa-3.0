#!/usr/bin/python
'''
Driver for the Lynxmotion BotBoarduino
'''

from smbus2 import SMBus
import time

class BOTBOARDUINO:
    def __init__(self,addr=0x08, register=0):
        try:
            self.bus = SMBus(1)
            self.addr = addr
            self.register = register
        except:
            print('Unable to initialize i2c connection')
        
    def send(self, data):
        try:
            self.bus.write_i2c_block_data(8, 0, data)
        except:
            print('Unable to send ', data)