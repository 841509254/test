import socket,os,sys

def main():
    if len(sys.argv)<3:
        print('参数错误')
        return
    address = (sys.argv[1],int(sys.argv[2]))
    # 创建UDP套接字
    cli = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 接收用户输入，包装后发给服务器
    while 1:
        name = input('请输入姓名:')
        msg = 'L ' + name
        #向服务器发消息
        cli.sendto(msg.encode(),address)
        #接收服务器反馈
        data,addr = cli.recvfrom(1024)
        if data.decode() == 'OK':
            print('您已进入聊天室')
            break
        else:
            # 打印不允许进入原因
            print(data.decode())
    #创建进程，子进程发消息，父进程接收消息
    pid = os.fork()
    if pid < 0:
        sys.exit('创建进程失败')
    #子进程发消息
    elif pid == 0:
        sendMsg(cli,name,address)
    #父进程收消息
    else:
        recvMsg(cli)
#子进程发消息函数
def sendMsg(cli,name,address):
    #发消息给服务端，服务端在进行转发
    while 1:
        try:
            msg = input('请发言(Quit退出)：')
        # 如果用户强制终止，捕捉异常，正常退出
        except KeyboardInterrupt:
            msg = 'Quit'
            # 退出
            if msg == 'Quit':
                data = 'Q '+ name
                cli.sendto(data.encode(),address)
                sys.exit('退出聊天室！')
        #包装消息
        data = 'C %s %s' % (msg,name)
        cli.sendto(data.encode(),address)
#父进程收消息函数
def recvMsg(cli):
    while 1:
        try:
            msg,addr = cli.recvfrom(1024)
            if msg.decode() == 'EXIT':
                os._exit(0)
            print(msg.decode() + '\n请发言(Quit退出)：',end='')
        except KeyboardInterrupt:
            os._exit(0)

    

    

if __name__ == "__main__":
    main()