import os
import socket
#__file__的意思的是 本python文件在os中的绝对路径
# os.path.dirname 的意思是找到文件所属的文件夹名称
# os.path.join的意思是拼凑文件的路径,并且可以在windows linux系统之间动态的切换 文件分隔符 '/','\'

dir_name = os.path.dirname(__file__)
# jpg_name = dir_name + '/' + '3_1.jpeg'

jpg_name = os.path.join(dir_name,'1.jpg')
jpg_name1 = os.path.join(dir_name,'3_1_copy1.jpg')
#print(jpg_name)
#rb read binary
#r模式是 read模式 普通字符串

#b""表示的是申明一个二进制的字符串对象

with open(jpg_name,'rb') as f:
    b_file = f.read()

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

addr = ('127.0.0.1',60000)

ss.connect(addr)

ss.sendall(b_file)

ss.close()

# with open(jpg_name1,'wb') as f:
#     f.write(b_file)