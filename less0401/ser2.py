import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ('127.0.0.1', 41901)
server.bind(server_addr)
print('服务器已经开启')

server.listen()

conn, conn_addr = server.accept()

while 1:
    try:
        msg = conn.recv(65535)

        msg = msg.decode()
        print('收到{}的消息:{}'.format(conn_addr, msg))

        return_msg = "已经收到你的消息--->" + msg

        conn.send(return_msg.encode())
    except Exception:
        break

conn.close()
server.close()
print(conn_addr)
print('服务器已经结束')