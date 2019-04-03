# 书写一个类似于qq群聊的聊天室,要求所有人都能收到所有人发送的消息,要求实现客户端和服务端
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 41903)
client.connect(server_addr)
while 1:
    try:
        msg = input('客户端说:')
        client.send(msg.encode())
        msg = client.recv(65535)
        print('服务器说:', msg.decode())
    except Exception:
        break
client.close()
print('链接已经完成')