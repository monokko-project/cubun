#!/usr/bin/python3
import socket
import time
import cv2
import struct
# def image_encoder():
#     encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
#     img = cv2.imread('/path_to_image/opencv-logo.png', 0) 

HOST = '192.168.40.102'
PORT = 10000

def start():
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # サーバーに接続
        s.connect((HOST, PORT))
        s.sendall(b'camera')

        frame_data = cv2.imread('../camera/out.jpg') 
        print(frame_data.shape)
        # フレームのサイズを送信
        # size = len(frame_data)
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        result, frame_data = cv2.imencode('.jpg', frame_data, encode_param)
        # print(size)
        size = len(frame_data)
        s.send(struct.pack('!I', size))
        # フレームデータを送信
        s.sendall(frame_data)

if __name__ == "__main__":
    # image_encoder()
    start()