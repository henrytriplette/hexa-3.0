from classes.rpi_RELAYBOARD import RELAYBOARD

import configparser

SERB_TOGGLE_BEC_SX = False
SERB_TOGGLE_BEC_DX = False
SERB_TOGGLE_LIGHT = False
SERB_TOGGLE_GIMBAL = False

try:

    # Read Configuration
    config = configparser.ConfigParser()
    config.read("config.ini")

    relays = {
        SERB_TOGGLE_BEC_SX: RELAYBOARD(config.SERB_TOGGLE_BEC_SX),
        SERB_TOGGLE_BEC_DX: RELAYBOARD(config.SERB_TOGGLE_BEC_DX),
        SERB_TOGGLE_LIGHT: RELAYBOARD(config.SERB_TOGGLE_LIGHT),
        SERB_TOGGLE_GIMBAL: RELAYBOARD(config.SERB_TOGGLE_GIMBAL)
    }

except:
    print("Relay board doesn't respond")

def setToggleButton(button_data):
    if (relays[button_data['key']]):
        if (button_data['data'] == True):
            relays[button_data['key']].activate()
        else:
            relays[button_data['key']].deactivate()
    else:
        print('No relay with key found')
        print(button_data)

def testConnection():
    for relay in relays:
        relay.test_connection()