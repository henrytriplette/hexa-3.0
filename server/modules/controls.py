# from classes.rpi_BOTBOARDUINO import BOTBOARDUINO
from modules import utility

data = [0, 0, 0, 128, 128, 128, 128]

def setControlsJoystick(joy_data):
    joy_data = utility.sanitizeJson(joy_data)

    # Pass the values
    data = [
        0,
        0,
        0,
        joy_data['left_joystick']['x'],
        joy_data['left_joystick']['y'],
        joy_data['right_joystick']['x'],
        joy_data['right_joystick']['y']
    ]

    # Smooth out data values
    data[3] = int(round(data[3]))
    data[4] = int(round(data[4]))
    data[5] = int(round(data[5]))
    data[6] = int(round(data[6]))

    print(data)

def setControlsButton(button_data):
    # button_data = utility.sanitizeJson(button_data)

    # Pass the values
    data = [
        0,
        0,
        button_data,
        128,
        128,
        128,
        128
    ]

    print(data)