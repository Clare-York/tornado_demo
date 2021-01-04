# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 9:52
@Author      : chengyao
@File        : applications.py
@introduce   :一些基础设定,一个是html等页面模版的存放位置,一个是css等静态文件的存放位置
"""
from config.routes import urls
import tornado.web
import os
from config.settings import *

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug": DEBUG,
    "autoreload": DEBUG,  # debug开启时自动重载应用
    "compiled_template_cache": False,  # 关闭模版缓存
    "static_hash_cache": False,  # 关闭静态文件缓存
    "serve_traceback": True  # 当一个异常在 RequestHandler 中没有捕获，将会生成一个包含调用栈信息的错误页
}
# handlers指的是url中的内容
application = tornado.web.Application(
    handlers=urls,
    **settings
)
