import socket
# 因为主机是ip4和tcp所以客户端一样需要使用ip4和tcp
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 41901)
# 可以端直接去链接地址 而不用去bind绑定地址并且listen
client.connect(server_addr)
#客户端不用写ip地址和端口号,socket帮助我们自动分配
client.send('我是客户端'.encode())
msg = client.recv(1460)
print('收到服务器发送过来的消息:',msg.decode())
client.close()
print('链接已经完成')