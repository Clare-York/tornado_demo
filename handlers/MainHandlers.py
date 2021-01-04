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
    用get的方式访问这个handler的话，就进入到get方法。
    这里没有写post的方法，如果用post的方法进入到这个handler会报错
    """

    def get(self):
        """
        处理get请求
        :return:
        """
        # write方法是字符串打印到浏览器页面。若返回模板html，需要用render
        self.write(self.request.method)
        self.write("Hello World")

    def post(self):
        """
        处理post请求
        :return:
        """
        self.write(self.request.method)
        self.write("Hello World")
