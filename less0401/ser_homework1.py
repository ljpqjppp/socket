# 作业:
#
# 1:书写一个socket服务器和客户端代码,要求客户端读取一个jpg或者png的媒体文件,
#   然后发送给服务器,服务器接受并保存在磁盘上面(位置随意)
# 2:写一个socket用来请求百度网页,并把请求下来的报文体部分保存
# 3:书写一个类似于百度的网站服务器,能够使用普通浏览器访问,只用返回简单的hello world即可

# 1:

import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 41903)
server.bind(server_addr)
print('服务开启')
server.listen()
conn, conn_addr = server.accept()
msg = conn.recv(65535)
# newjpg =
print('收到客户端图片')
retuen_msg = '图片已经收到'
conn.send(retuen_msg.encode())

conn.close()
server.close()
print('服务器关闭')

