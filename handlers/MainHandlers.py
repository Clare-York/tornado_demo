# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 9:55
@Author      : chengyao
@File        : MainHandlers.py
@introduce   : 根路由对应的执行逻辑-模版
"""
from abc import ABC

import tornado.web


class MainHandler(tornado.web.RequestHandler, ABC):
    """
    根路由对应逻辑
    用get方式访问，就进入到get方法。
    write方法是字符串打印到浏览器页面。若返回模板html，需要用render
    """

    def get(self):
        """
        处理get请求
        :return:
        """
        self.render("index.html")

    def post(self):
        """
        处理post请求
        :return:
        """
        self.write(self.request.method)

        self.write("<p></p>")

        self.write("Hello World")
