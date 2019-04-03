import os
import socket
dir_name = os.path.dirname(__file__)
jpg_name = os.path.join(dir_name, '1.jpg')
b_file = b''
with open(jpg_name, 'rb') as f:
    tmp =f.read()
    b_file += tmp
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 41903)
client.connect(server_addr)
client.send(b_file)
msg = client.recv(65535)
print('收到服务端消息', msg.decode())
client.close()
print('连接完成')