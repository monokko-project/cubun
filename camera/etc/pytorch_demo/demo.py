import time

import torch
import numpy as np
from torchvision import models, transforms

import cv2
from PIL import Image
from picamera2 import Picamera2
from libcamera import controls

import imagenet_stubs
from imagenet_stubs.imagenet_2012_labels import label_to_name


torch.backends.quantized.engine = 'qnnpack'


# Picameraを起動
camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={
	"format": 'XRGB8888',
    "size": (720, 480)
	# "size": (224, 224)
}))
camera.start()
camera.set_controls({'AwbMode': 0})
# camera.set_controls('AfMode')


def read_camera(camera):
    
    # カメラから画像を取得
    image = camera.capture_array()

    # 画像が3チャンネル以外の場合は3チャンネルに変換する
    channels = 1 if len(image.shape) == 2 else image.shape[2]
    if channels == 1:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    if channels == 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        
    return image

preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

net = models.quantization.mobilenet_v2(pretrained=True, quantize=True)
# jit model to take it from ~20fps to ~30fps
net = torch.jit.script(net)

started = time.time()
last_logged = time.time()
frame_count = 0

with torch.no_grad():
    while True:
        # read frame
        # ret, image = cap.read()
        image = read_camera(camera)
        if image is None:
            raise RuntimeError("failed to read frame")

        # convert opencv output from BGR to RGB
        # image = image[:, :, [2, 1, 0]]
        # permuted = image
        
        cv2.imwrite('input_image.jpg', image)

        '''
        # preprocess
        input_tensor = preprocess(image)

        # create a mini-batch as expected by the model
        input_batch = input_tensor.unsqueeze(0)

        # run model
        output = net(input_batch)
        # do something with output ...
        top = list(enumerate(output[0].softmax(dim=0)))
        top.sort(key=lambda x: x[1], reverse=True)
        
        # for idx, val in top[:10]:
        #     print(f"{val.item()*100:.2f}% {label_to_name(idx)}")
        idx, val = top[0]
        print(f"{val.item()*100:.2f}% {label_to_name(idx)}")
        
        # log model performance
        frame_count += 1
        now = time.time()
        if now - last_logged > 1:
            print(f"{frame_count / (now-last_logged)} fps")
            last_logged = now
            frame_count = 0
        '''