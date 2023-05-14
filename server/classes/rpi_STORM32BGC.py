#!/usr/bin/python
'''
Driver for the Gimbal Board
'''

from time import sleep

# Make sure you install required libraries:
# https://gpiozero.readthedocs.io/en/stable/installing.html
# Pin numbering as follows:
# https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering
from gpiozero import Servo, AngularServo


class STORM32BGC:
    def __init__(self, settings):

        self.settings = settings

        self.gimbalX = AngularServo(int(settings['PWM_GIMBAL_X']), min_angle=float(settings['PWM_GIMBAL_X_min_angle']), max_angle=float(settings['PWM_GIMBAL_X_max_angle']))
        self.gimbalX.angle = float(settings['PWM_GIMBAL_X_start_angle'])

        self.gimbalY = AngularServo(int(settings['PWM_GIMBAL_Y']), min_angle=float(settings['PWM_GIMBAL_Y_min_angle']), max_angle=float(settings['PWM_GIMBAL_Y_max_angle']))
        self.gimbalY.angle = float(settings['PWM_GIMBAL_Y_start_angle'])

        self.gimbalZ = AngularServo(int(settings['PWM_GIMBAL_Z']), min_angle=float(settings['PWM_GIMBAL_Z_min_angle']), max_angle=float(settings['PWM_GIMBAL_Z_max_angle']))
        self.gimbalZ.angle = float(settings['PWM_GIMBAL_Z_start_angle'])

        self.gimbalReset = Servo(int(settings['PWM_GIMBAL_RESET']))

    def play(self, gimbal_data):
        self.gimbalX.angle = float(gimbal_data['x'])
        self.gimbalY.angle = float(gimbal_data['y'])
        self.gimbalZ.angle = float(gimbal_data['z'])

        print(self.gimbalX.angle, self.gimbalY.angle, self.gimbalZ.angle)

    def reset(self):
        self.gimbalX.angle = float(self.settings['PWM_GIMBAL_X_start_angle'])
        self.gimbalY.angle = float(self.settings['PWM_GIMBAL_Y_start_angle'])
        self.gimbalZ.angle = float(self.settings['PWM_GIMBAL_Z_start_angle'])

        self.gimbalReset.min()
        self.gimbalReset.max()
        sleep(0.1)
        self.gimbalReset.min()