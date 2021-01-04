# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 14:16
@Author      : chengy_work@foxmail.com
@File        : PageNotFoundHandlers.py
@Introduce   : 自定义404处理
"""
from abc import ABC
from Config.log import errlogger
import tornado.web


class PageNotFoundHandler(tornado.web.RequestHandler, ABC):
    """
    自定义404
    """

    def get(self):
        """
        pass
        :return:
        """
        errlogger.debug("Remote_IP: %s" % self.request.remote_ip)
        errlogger.debug("Method: %s" % self.request.method)
        errlogger.error("404 Not Found")
        self.render("404.html")

    def post(self):
        """
        pass
        :return:
        """
        errlogger.debug("Remote_IP: %s" % self.request.remote_ip)
        errlogger.debug("Method: %s" % self.request.method)
        errlogger.error("404 Not Found")
        self.render("404.html")
