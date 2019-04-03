import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 41903)
server.bind(server_addr)
print('服务器开启')
server.listen()
while 1:
    try:
        conn, conn_addr = server.accept()
    except Exception:
        break
    while 1:
        try:
            msg = conn.recv(65535)
            if not msg:
                break
            msg = msg.decode()
            print('收到{}的消息：{}'.format(conn_addr, msg))
            return_msg = '已收到消息'+ msg
            conn.send(return_msg.encode())
        except Exception:
            break
    conn.close()
    print('{}的链接断开'.format(conn_addr))
server.close()
print('服务器断开')