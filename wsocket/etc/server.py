#!/usr/bin/env python3
import socket
import time
def start():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as streamSocket:
        # 10000番ポートでサーバーを立ち上げる
        streamSocket.bind(('0.0.0.0', 10000))
        # 1クライアントだけ受け入れる
        streamSocket.listen(1)
        # クライアントからの接続待ち
        clientSocket, addr = streamSocket.accept()
        # クライアントへメッセージ送信
        clientSocket.sendall(b'from server 1st message')
        time.sleep(1)
        # クライアントへメッセージ送信
        clientSocket.sendall(b'from server 2st message')
        # クライアントからのメッセージ受信待ち
        byteData = clientSocket.recv(1024)
        print(byteData)
        # クライアントからのメッセージ受信待ち
        byteData = clientSocket.recv(1024)
        print(byteData)
        
if __name__ == "__main__":
    start()