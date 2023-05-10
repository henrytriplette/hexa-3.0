from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput
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
    #buffer = StreamingOutput()
    while True:
        with Picamera2 as camera:
            camera.configure(camera.create_video_configuration(main={"size": (640, 480)}))
            output = StreamingOutput()
            camera.start_recording(JpegEncoder(), FileOutput(output))
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + output.frame + b'\r\n')