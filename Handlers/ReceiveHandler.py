# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/8 16:12
@Author      : chengy_work@foxmail.com
@File        : ReceiveHandler.py
@Introduce   : 接受消息，然后调用推送
"""
from abc import ABC
from tornado.web import RequestHandler
from Core.PushCore import PushCore
from loguru import logger


class ReceiveHandler(RequestHandler, ABC):
    """
    pass
    """

    def get(self):
        """
        pass
        :return:
        """
        self.render("socket.html")

    def post(self):
        uuid = self.get_argument("uuid", "")
        if not uuid:
            uuid = None
        core = self.get_argument("core")
        memory_total = self.get_argument("memory_total")
        disk_total = self.get_argument("disk_total")
        cpu_used = self.get_argument("cpu_used") + "%"
        memory_used = self.get_argument("memory_used") + "%"
        disk_used = self.get_argument("disk_used") + "%"
        I = self.get_argument("network_input") + "K/s"
        O = self.get_argument("network_output") + "K/s"
        message = {"core": core, "memory_total": memory_total, "disk_total": disk_total, "cpu_used": cpu_used,
                   "memory_used": memory_used, "disk_used": disk_used, "network_input": I, "network_output": O}
        logger.success(message)
        PushCore().trigger(message, uuid)  # 接收到消息之后推送
