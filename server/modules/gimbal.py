
from classes.rpi_STORM32BGC import STORM32BGC

import configparser

# Read Configuration
config = configparser.ConfigParser()
config.read("config.ini")

settings = {
    'PWM_GIMBAL_X': config['gpio']['PWM_GIMBAL_X'],
    'PWM_GIMBAL_X_min_angle': config['gimbal']['PWM_GIMBAL_X_min_angle'],
    'PWM_GIMBAL_X_max_angle': config['gimbal']['PWM_GIMBAL_X_max_angle'],
    'PWM_GIMBAL_X_start_angle': config['gimbal']['PWM_GIMBAL_X_start_angle'],
    'PWM_GIMBAL_Y': config['gpio']['PWM_GIMBAL_Y'],
    'PWM_GIMBAL_Y_min_angle': config['gimbal']['PWM_GIMBAL_Y_min_angle'],
    'PWM_GIMBAL_Y_max_angle': config['gimbal']['PWM_GIMBAL_Y_max_angle'],
    'PWM_GIMBAL_Y_start_angle': config['gimbal']['PWM_GIMBAL_Y_start_angle'],
    'PWM_GIMBAL_Z': config['gpio']['PWM_GIMBAL_Z'],
    'PWM_GIMBAL_Z_min_angle': config['gimbal']['PWM_GIMBAL_Z_min_angle'],
    'PWM_GIMBAL_Z_max_angle': config['gimbal']['PWM_GIMBAL_Z_max_angle'],
    'PWM_GIMBAL_Z_start_angle': config['gimbal']['PWM_GIMBAL_Z_start_angle'],
    'PWM_GIMBAL_RESET': config['gpio']['PWM_GIMBAL_RESET'],
}

storm32gbc = STORM32BGC(settings)

def setGimbalPosition(button_data):
    storm32gbc.play(button_data)
    # print(button_data)

def setGimbalReset(button_data):
    storm32gbc.reset()
    # print(button_data)