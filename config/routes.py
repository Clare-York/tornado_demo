# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 9:53
@Author      : chengyao
@File        : routes.py
@introduce   : 路由文件
"""
from handlers.MainHandlers import MainHandler
from handlers.TestHandlers import TestHandler

# 将路由存入到列表中，后续注册对应视图到server端，告诉server端不同地址，
urls = [
    (r"/", MainHandler),  # 根路由
    (r"/test", TestHandler),  # 测试

]
