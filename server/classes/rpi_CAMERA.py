from picamera2 import Picamera2 as picamera #used for camera control
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput 

from threading import Condition
import io

# Based on https://github.com/raspberrypi/picamera2/issues/366
class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        self.frame = None
        self.condition = Condition()

    def write(self, buf):
        with self.condition:
            self.frame = buf
            self.condition.notify_all()

class CAMERA:
    def genFrames():
        global camera, buffer #camera must be global to allow photos while streaming
        try: camera #checks if camera is initialized yet
        except NameError: #if not, initializes camera:
            # try:
            camera = picamera()
            buffer = StreamingOutput()
            camera.configure(camera.create_video_configuration(main={"size": (640, 480)}))
            camera.start_recording(JpegEncoder(), FileOutput(buffer))

        while True:
            with buffer.condition:
                buffer.condition.wait()
                frame = buffer.frame
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')