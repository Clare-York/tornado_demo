# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/8 16:13
@Author      : chengy_work@foxmail.com
@File        : ConnectHandler.py
@Introduce   : websocket核心方法
"""
from abc import ABC
from tornado.websocket import WebSocketHandler
from Core.ConnectCore import PushCore


class ConnectHandler(WebSocketHandler, ABC):
    """
    pass
    """

    def check_origin(self, origin):
        """
        重写同源检查 解决跨域问题
        :param origin:
        :return:
        """
        print("跳过同源检查...")
        return True

    def open(self):
        """
        新的websocket连接后被调动
        :return:
        """
        print("新client端接入...")
        self.uuid = PushCore().user_connect(self)
        self.write_message('Welcome')

    def on_close(self):
        """
        websocket连接关闭后被调用
        :return:
        """
        print("client端断开连接...")
        PushCore().user_remove(self.uuid)  # client断开连接后remove user

    def on_message(self, message):
        """
        接收到客户端消息时被调用,常用于对话，或接收特定指令
        :param message:
        :return:
        """
        print("接收到client端传递的消息：%s" % message)
        self.write_message('new message :' + message)
