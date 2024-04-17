import cv2
from picamera2 import Picamera2
# from libcamera import controls

camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={
	"format": 'XRGB8888',
	"size": (640, 480)
}))
camera.start()


"""
>>> camera.camera_ctrl_info.keys()
dict_keys(['NoiseReductionMode', 'ScalerCrop', 'Sharpness', 'AwbEnable', 'AeEnable', 'ExposureTime', 'AeConstraintMode', 'Brightness', 'ColourGains', 'AnalogueGain', 'Contrast', 'AeMeteringMode', 'Saturation', 'AeExposureMode', 'AwbMode', 'ExposureValue', 'FrameDurationLimits'])
"""

""" https://libcamera.org/api-html/namespacelibcamera_1_1controls.html """
camera.set_controls({'AwbMode': 0})
# camera.set_controls('AfMode')

image = camera.capture_array()

# change to 3 channels if it isnt
channels = 1 if len(image.shape) == 2 else image.shape[2]
if channels == 1:
	image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
if channels == 4:
	image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

# save as jpg
cv2.imwrite('test.jpg', image)