import cv2
# from time import time
import time
from camera.model.coca import Image2Text
from camera.utils.camera import Camera
from wsocket.client import Client
from audio.audio import Audio
from nlp.model import NLPmodel

c = Camera()
# it = Image2Text()

HOST = '192.168.40.102'
PORT = 10000
AUDIO_DEVICE = 'hw:0,0' 

sclient = Client(HOST, PORT)
aud = Audio(AUDIO_DEVICE)
nlp_ja = NLPmodel("ja_ginza")

start = time.time()
interval_sec = 5
sleep_time = 5

cubun_noun_memory = []
same_text_count = 0

def main():
    global same_text_count

    while True:
        aud.speack_ojtalk("まわりを読み込むきゅぶ", "f")
        time.sleep(aud.out_duration + 0.3)
        frame = c.caputure("out.jpg")

        aud.speack_ojtalk("ふむふむ", "f")
        time.sleep(aud.out_duration + 0.3)
        out, trans_out = sclient.send_image("out.jpg")
        text = out.decode()
        text_jp = trans_out.decode()
        # aud.speack_ojtalk(text, "f")
        
        
        print(text)
        jp_nouns = nlp_ja.extract_noun(text_jp)
        print(jp_nouns)

        # text_jp = nlp_en.trans_en_to_jp(text)
        print(text_jp)
        for mem in cubun_noun_memory:
            if mem in jp_nouns:
                jp_nouns.remove(mem)

        if jp_nouns:
            for idx , n in enumerate(jp_nouns):
                aud.speack_ojtalk(f"{n}みたいなもの...がある...", "f")
                time.sleep(aud.out_duration + 0.3)

                if idx == len(jp_nouns) -2 :
                    aud.speack_ojtalk(f"さらに..", "f")
                    time.sleep(aud.out_duration + 0.3)
                
                cubun_noun_memory.append(n)
            pre_text = text
        else:
            if pre_text == text:
                same_text_count += 1
            
            if same_text_count >= 5:
                aud.speack_ojtalk(f"あたらしいものが...みたくなってきたぶん", "f")
                time.sleep(aud.out_duration + 0.3)
                
        
        
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