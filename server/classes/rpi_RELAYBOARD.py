#!/usr/bin/python
'''
Driver for the Relay Board
'''

from time import sleep

# Make sure you install required libraries:
# https://gpiozero.readthedocs.io/en/stable/installing.html
# Pin numbering as follows:
# https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering
from gpiozero import OutputDevice, GPIOZeroError

class RELAYBOARD:
    def __init__(self, pin, active_high=False, initial_value=False):
        try:
            self.relay = OutputDevice(pin, active_high=active_high, initial_value=initial_value)
            self.state = self.get_state()
        except GPIOZeroError:
            print('A GPIO Zero error occurred')

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
        sleep(1)
        self.relay.off()