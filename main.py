# quick hack by savraj
# picamera docs
# https://picamera.readthedocs.io/en/release-1.13/api_camera.html

from picamera import PiCamera
import time
print("program starting up. Press ENTER to capture an image, CTRL-C to quit.")

with PiCamera() as camera:
    camera.start_preview()
    try:
        for i, filename in enumerate(
                camera.capture_continuous('img_{timestamp:%H-%M-%S}-{counter:03d}.jpg')):
            print(filename)
            time.sleep(2)
            input("press Enter to snap an image.")
    finally:
        camera.stop_preview()
