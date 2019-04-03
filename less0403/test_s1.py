import socket
import os
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('127.0.0.1', 5001)
ss.bind(addr)
print('服务开启')
ss.listen()
while 1:
    cnn, cnn_add = ss.accept()
    while 1:
        msg = cnn.recv(65535)
        print('客户消息：{}'.format(msg.decode()))
        msg1 = input('服务器消息：')
        cnn.send(msg1.encode())
        if not msg:
            break

print('服务器结束')