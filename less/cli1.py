import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ('0.0.0.0', 41901)
client.connect(server_addr)
client.send('我是客户端'.encode())
msg = client.recv(1460)
print('收到服务端发送的消息', msg.decode())
client.close()
print('连接已经完成')