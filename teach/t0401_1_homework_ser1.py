import socket
import os

dir_name = os.path.dirname(__file__)
# jpg_name = dir_name + '/' + '3_1.jpeg'

jpg_name = os.path.join(dir_name,'3_1_server1.jpg')

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

addr = ('127.0.0.1',60000)
ss.bind(addr)

ss.listen()
#为什么这样写 就是因为别人写的 返回两个值 第一个是链接对象 第二个是地址
conn,addr = ss.accept()

b_file = b""
while 1:
    msg = conn.recv(65535)
    if not msg:
        break
    b_file += msg

with open(jpg_name,'wb') as f:
    f.write(b_file)

conn.close()
ss.close()