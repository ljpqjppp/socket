import socket
# 选择IPV4和TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置服务器ip和端口
server_addr = ('0.0.0.0', 41901)
# 绑定这个地址和端口
server.bind(server_addr)
print('服务已经开启')
# 开启监听
server.listen()
# 定义连接对象和连接地址 为了接收客户进来
conn, conn_addr = server.accept()
# 客户数据过来的最大单位数
msg = conn.recv(65535)
# 加上encode 把普通字符串变成二进制 decode是反之
print('收到客户端发送的消息', msg.decode())
return_msg = '消息已经收到了'
# 把服务器发给客户端的消息从STR转为二进制
conn.send(return_msg.encode())
# print(conn)
conn.close()
server.close()
print(conn_addr)
print('服务已经结束')
