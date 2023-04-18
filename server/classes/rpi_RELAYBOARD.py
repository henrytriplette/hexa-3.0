#!/usr/bin/python
'''
Driver for the Relay Board
'''

import sys
import time

# Make sure you install required libraries:
# https://gpiozero.readthedocs.io/en/stable/installing.html
# Pin numbering as follows:
# https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering
from gpiozero import OutputDevice

class RELAYBOARD:
    def __init__(self, pin, active_high=True, initial_value=True):
        self.relay = OutputDevice(pin, active_high=active_high, initial_value=initial_value)
        self.state = self.get_state()

    def activate(self):
        self.relay.on()
        self.state = self.get_state()

    def deactivate(self):
        self.relay.off()
        self.state = self.get_state()

    def get_state(self):
        return self.relay.value

    def test_connection(self):
        '''
        test the pi's ability to control a relay
        do this BEFORE hooking up anything to the relay and watch LED on the relay board
        '''
        self.relay.on()
        time.sleep(1)
        self.relay.off()