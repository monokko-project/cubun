#!/usr/bin/python3
import socket
import time
import cv2
import struct

# HOST = '192.168.40.102'
# PORT = 10000

class Client:
    def __init__(self, host, port):
        self.host = host 
        self.port = port

    def send_image(self, path='../camera/out.jpg'):
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            # サーバーに接続
            s.connect((self.host, self.port))
            s.sendall(b'camera')

            frame_data = cv2.imread(path) 
            print(frame_data.shape)
            # フレームのサイズを送信
            # size = len(frame_data)
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            _, frame_data = cv2.imencode('.jpg', frame_data, encode_param)
            
            

            # image size
            size = len(frame_data)
            s.send(struct.pack('!I', size))

            # send frame data
            s.sendall(frame_data)