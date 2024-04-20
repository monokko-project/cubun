import cv2
from time import time

from model.coca import Image2Text
from utils.camera import Camera


c = Camera()
it = Image2Text()

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

frame = c.caputure("out.jpg")
text = it.run("out.jpg")
print(text)

