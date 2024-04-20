import cv2
from time import time

from camera.model.coca import Image2Text
from camera.utils.camera import Camera
from wsocket.client import Client

c = Camera()
# it = Image2Text()

HOST = '192.168.40.102'
PORT = 10000
sclient = Client(HOST, PORT)

start = time()
interval_sec = 15


""" 
while True:
    frame = c.capture()
    # c.show(frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    
    if time() - start > interval_sec:
        ## save frame as image
        # cv2.imwrite("out.jpeg", frame)
        
        # print("Capturing image...")
        start = time()
        text = it.run("out.jpeg")
        names, probs = y.get_results("out.jpeg")


        print(text)
        break
"""

while True:
    frame = c.caputure("out.jpg")
    sclient.send_image("out.jpg")
    # text = it.run("out.jpg")
    # print(text)
    print(time() - start)

# a close - up view of a white wall . 
# 231.3489875793457