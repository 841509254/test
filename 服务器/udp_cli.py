# -*- coding:utf-8 -*-

import socket

address = ('127.0.0.1',8888)

cli = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)



while True:
    msg = input('想发什么？')
    if msg:
        cli.sendto(msg.encode(),address)
    else:
        cli.sendto(msg.encode(), address)
        break
    data,addr = cli.recvfrom(1024)
    print(data.decode(),addr)

cli.close()
