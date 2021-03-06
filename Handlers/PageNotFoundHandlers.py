# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 14:16
@Author      : chengy_work@foxmail.com
@File        : PageNotFoundHandlers.py
@Introduce   : 请求未定义路由时的自定义404处理
"""
from abc import ABC
from loguru import logger
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
        self.render("404.html")
        logger.warning("%s,%s,%s" % (self.request.method, self.request.remote_ip, self.request.uri))
        logger.warning(tornado.web.HTTPError(404))
        self.set_status(404)

    def post(self):
        """
        pass
        :return:
        """
        self.render("404.html")
        logger.warning("%s,%s,%s" % (self.request.method, self.request.remote_ip, self.request.uri))
        logger.warning(tornado.web.HTTPError(404))
        self.set_status(404)
