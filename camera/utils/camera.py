import cv2
from picamera2 import Picamera2
# from libcamera import controls


class Camera:
    def __init__(self):
        self.camera = Picamera2()
        self.camera.configure(self.camera.create_preview_configuration(main={
            "format": 'XRGB8888',
            "size": (640, 480)
        }))

    def caputure(self, image_path="image_path.jpg"):
        self.camera.start()
        self.camera.set_controls({'AwbMode': 0})
        image = self.camera.capture_array()

        # change to 3 channels if it isnt
        channels = 1 if len(image.shape) == 2 else image.shape[2]
        if channels == 1:
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        if channels == 4:
            image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

        # save as jpg
        cv2.imwrite(image_path, image)

""" debug """
# c = Camera()
# c.caputure("util_cam.jpg")