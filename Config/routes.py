# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 9:53
@Author      : chengy_work@foxmail.com
@File        : routes.py
@Introduce   : 路由文件
"""

from Handlers.MainHandlers import MainHandler
from Handlers.TestHandlers import TestHandler
from Handlers.PageNotFoundHandlers import PageNotFoundHandler

# 将路由存入到列表中，后续注册对应视图到server端，告诉server端不同地址，
urls = [
    (r"/", MainHandler),  # 根路由
    (r"/test", TestHandler),  # 测试

    (r".*", PageNotFoundHandler),  # 自定义404页，这一条放在所有路由的最后，否则下方的路由均被导向到404页
]
