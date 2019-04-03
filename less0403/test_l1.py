import socket
ss = ('127.0.0.1', 5001)
cnn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cnn.connect(ss)
while 1:
    try:
        msg = str(input('客户消息：'))
        cnn.send(msg.encode())
        msg1 = cnn.recv(65535)
        print('服务器说：{}'.format(msg1.decode()))
    except Exception:
        break

cnn.close()
print('链接已经完成')