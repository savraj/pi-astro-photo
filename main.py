from picamera import PiCamera
import time
import keyboard
from datetime import datetime
print("program starting up. Press SPACEBAR to capture an image.")
print("Press Q or ESCAPE to quit.")

with PiCamera() as camera:
    camera.start_preview()
    try:
        for i, filename in enumerate(
                camera.capture_continuous('img_{timestamp:%H-%M-%S}-{counter:03d}.jpg')):
            print(filename)
            time.sleep(2)
            input("press a key to move on.")
    finally:
        camera.stop_preview()



# 
# with PiCamera() as camera:
#     camera.resolution = (1920, 1080)
#     camera.start_preview()
#     time.sleep(5)

#     print('here we go....')

#     def save_photo():
#         ts = datetime.now().replace(microsecond=0)
#         camera.capture(f'{ts.isoformat()}.jpg')

#     def stop():
#         print("It should have worked?")
#         camera.stop_preview()
#         camera.close()
#         exit()


#     keyboard.add_hotkey('space', save_photo)
#     keyboard.add_hotkey('q', stop)
#     keyboard.add_hotkey('esc', stop)

#     for i, filename in enumerate(
#             camera.capture_continuous('image{counter:02d}.jpg')):
#         print(filename)
