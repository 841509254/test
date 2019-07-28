# -*- coding:utf-8 -*-
import socket

# svr = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#
# svr.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#
# svr.bind(('0.0.0.0',8888))
#
# print('等待客户端连接...')
#
# while True:
#     data,addr = svr.recvfrom(1024)
#     if data:
#         print(data.decode(),addr)
#     else:
#         break
#     svr.sendto('收到消息：'.encode(),addr)
#
# svr.close()



svr = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

svr.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

svr.bind(('0.0.0.0',8888))

print('等待连接：')

while 1:
    data,addr = svr.recvfrom(1024)
    if data:
        print(data.decode(),addr)
    else:
        break
    svr.sendto('收到消息啦'.encode(),addr)

svr.close()













