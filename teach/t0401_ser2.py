import socket
# 使用方式
# 1. 初始化socket对象
# socket里面 第一个写使用哪个网络层协议 第二写使用哪个运输层协议
# 网络层 socket.AF_INET 表示的是使用ipv4协议 socket.AF_INET6表示ipv6
# 运输层 socket.SOCK_STREAM 表示的tcp协议 SOCK_DGRAM 表示的是udp协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 绑定ip和端口
# 127.0.0.1 --> 本地回环网 loop 如果绑定该地址 其他人不能访问
# 0.0.0.0 --> 会自动换算成路由器分配的局域网地址 相当于 10.2.1.78
# 其他人可以访问,但是ip地址会变成局域网地址 不会是0.0.0.0
# 255.255.255.255 --> 广播地址
# 10.2.1.78  ---> 局域网地址
server_addr = ('127.0.0.1', 41901)
server.bind(server_addr)
print('服务器已经开启')
# 3. 监听这个地址
server.listen()
# 4. 监听这个地址之后,就需要接收服务
# conn表示链接对象 addr链接的地址
# 有链接进来才会向下执行,无连接进来就会阻塞
conn, conn_addr = server.accept()
# conn是一个对象
# 1460 一次性能收1460B的数据 多少消息
# mss 报文最大量 tcp默认是 1460 因为链路层一般最大能接受1500B的数据量
# tcp 20B ip 20B 1500-40 = 1460B
# 理论最大值是 65535-40 = 65495B
while 1:
    try:
        msg = conn.recv(65535)
        #收到的消息是二进制
        #把二进制数据转换成字符串
        msg = msg.decode()
        print('收到{}的消息:{}'.format(conn_addr,msg))
        # 是一个tuple
        return_msg = "已经收到你的消息--->"+ msg
        #加上encode 把普通字符串变成二进制
        conn.send(return_msg.encode())
    except Exception:
        break

# unicode
# utf8
# ascii
# gbk
conn.close()
server.close()
print(conn_addr)
print('服务器已经结束')