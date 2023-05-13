from classes.rpi_CAMERA import CAMERA
from flask import Response

def genFrames():
    return Response(CAMERA.genFrames(), mimetype='multipart/x-mixed-replace; boundary=frame')
