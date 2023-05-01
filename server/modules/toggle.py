from classes.rpi_RELAYBOARD import RELAYBOARD

import configparser

# Read Configuration
config = configparser.ConfigParser()
config.read("config.ini")

relays = {
    'SERB_TOGGLE_BEC_SX': RELAYBOARD(config['gpio']['SERB_TOGGLE_BEC_SX']),
    'SERB_TOGGLE_BEC_DX': RELAYBOARD(config['gpio']['SERB_TOGGLE_BEC_DX']),
    'SERB_TOGGLE_LIGHT': RELAYBOARD(config['gpio']['SERB_TOGGLE_LIGHT']),
    'SERB_TOGGLE_GIMBAL': RELAYBOARD(config['gpio']['SERB_TOGGLE_GIMBAL'])
}

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