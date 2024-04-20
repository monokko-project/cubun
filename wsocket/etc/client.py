#!/usr/bin/python3
import socket
import time
import cv2
import struct
# def image_encoder():
#     encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
#     img = cv2.imread('/path_to_image/opencv-logo.png', 0) 



def start():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as streamSocket:
        # RaspberryPiへ10000番ポートで接続
        # ラズパイはデフォルトでraspberrypi.localというPC名が設定されています
        # streamSocket.connect(('raspberrypi.local', 10000))
        streamSocket.connect(('192.168.40.102', 10000))
        # サーバーからのメッセージ受信待ち
        byteData = streamSocket.recv(1024)
        print(byteData)
        # サーバーからのメッセージ受信待ち
        byteData = streamSocket.recv(1024)
        print(byteData)
        time.sleep(1)

        # img = cv2.imread('../out.jpg', 0) 
        # size = len(img)
        # streamSocket.send(struct.pack('!I', size))
        # streamSocket.sendall(img)

        # サーバーへメッセージ送信
        streamSocket.sendall(b'from client 1st message: ohayo')
        time.sleep(1)
        # サーバーへメッセージ送信
        streamSocket.sendall(b'from client 2st message')
    

    

if __name__ == "__main__":
    # image_encoder()
    start()