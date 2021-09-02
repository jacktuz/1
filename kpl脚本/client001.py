#################服务端结构
# tcpc = socket()    # 创建客户端套接字
# tcpc.connect()    # 尝试连接服务器
# while True:        # 通讯循环
#     tcpc.send()/tcpc.recv()    # 对话(发送/接收)
# tcpc.close()      # 关闭客户套接字



#!/usr/bin/python3
# -*-coding:utf-8 -*-
from socket import *

#服务端 端口号、IP
HOST = '10.11.7.13'
PORT = 21566
ADDR = HOST,PORT

tcpC = socket(AF_INET, SOCK_STREAM)    #创建socket对象
tcpC.connect(ADDR)      #连接服务器

while True:
    data = input("请输入给服务端的信息：")
    if data == "exit":
        break
    else:
        tcpC.send(data.encode('utf-8'))    #发送消息
        data = tcpC.recv(1024)    #读取消息

tcpC.close() #关闭客户端