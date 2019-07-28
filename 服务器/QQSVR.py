'''
名称：局域网聊天室
环境：python3.5
技术：socket fork
'''
import socket,os,sys

#创建网络连接
def main():
    #创建UDP套接字
    svr = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #设置端口复用
    svr.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    #绑定地址
    address=('0.0.0.0',8888)
    svr.bind(address)
    #创建子进程,子进程负责管理员喊话，父进程和客户端交互
    pid = os.fork()
    if pid < 0:
        sys.exit('进程创建失败！')
    elif pid == 0:
        #子进程负责管理员发送消息
        while 1:
            msg = input('管理员消息：')
            #对消息进行包装
            data = 'C %s 管理员' % msg
            #父进程在监听，把消息发给父进程
            svr.sendto(data.encode(),address)
    else:
        #父进程处理客户端的各种请求
        doRequest(svr)

#处理客户端请求的函数
def doRequest(svr):
    user = {}
    while 1:
        # 接收消息
        msg,addr = svr.recvfrom(1024)
        msglist = msg.decode().split(' ')
        
        if msglist[0] == 'L':
            name = ' '.join(msglist[1:])
            doLogin(svr,user,name,addr)
        elif msglist[0] == 'C':
            name = msglist[-1]
            data = ' '.join(msglist[1:-1])
            #发给其他所有成员
            doChat(svr,data,user,name)
        elif msglist[0] == 'Q':
            name = ' '.join(msglist[1:])
            doQuit(svr,name,user)
#聊天函数
def doChat(svr,data,user,name):
    # 丰满消息
    msg = '\n%s说：%s' % (name,data)
    print(msg)
    for u in user:
        #发给其他成员
        if u != name:
            svr.sendto(msg.encode(),user[u])
#处理客户端退出函数
def doQuit(svr,name,user):
    #　通知其他成员
    msg = '\n%s退出聊天室' % name
    for u in user:
        #发给其他成员
        if u != name:
            svr.sendto(msg.encode(),user[u])
        else:
            svr.sendto(b'EXIT',user[u])
    # 从存储结构中删除
    del user[name]




#进入聊天室请求处理函数：
def doLogin(svr,user,name,addr):
    #{name:addr}
    if (name in user) or ('管理员' == name) or (chr(32) in name) or ('　' in name):
        svr.sendto('该用户已存在或不合法'.encode(),addr)
        return
    # 名字不存在，发送ＯＫ给客户端，允许进入
    svr.sendto('OK'.encode(),addr)
    # 先通知其他人
    msg = '\n欢迎 %s 进入聊天室！' % name
    for u in user:
        svr.sendto(msg.encode(),user[u])
    # 加入存储结构user中
    user[name] = addr
    print(user)

    if __name__ == "__main__":
        main()






