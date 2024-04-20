import cv2
# from time import time
import time
from camera.model.coca import Image2Text
from camera.utils.camera import Camera
from wsocket.client import Client
from audio.audio import Audio

c = Camera()
# it = Image2Text()

HOST = '192.168.40.102'
PORT = 10000
AUDIO_DEVICE = 'hw:0,0' 

sclient = Client(HOST, PORT)
aud = Audio(AUDIO_DEVICE)

start = time.time()
interval_sec = 5
sleep_time = 5

def main():
    while True:
        aud.speack_ojtalk("まわりを読み込むきゅぶ", "f")
        time.sleep(aud.out_duration + 0.3)
        frame = c.caputure("out.jpg")

        aud.speack_ojtalk("ふむふむ", "f")
        time.sleep(aud.out_duration + 0.3)
        out = sclient.send_image("out.jpg")
        text = out.decode()
        # aud.speack_ojtalk(text, "f")
        
        
        print(text)
        # out = "cup"
        if "cup" in text or "mug" in text:
            aud.speack_ojtalk("カップンが検知されましたきゅぶ．ヘッドマウントディスプレイを装着して様子を見てみるきゅぶ", "f")
            time.sleep(aud.out_duration + 0.3)
        # text = it.run("out.jpg")
        # print(text)
        print(time.time() - start)

        time.sleep(sleep_time)

# a close - up view of a white wall . 
# 231.3489875793457


if __name__ == "__main__":
    main()