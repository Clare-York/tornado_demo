# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 9:52
@Author      : chengy_work@foxmail.com
@File        : Applications.py
@Introduce   : 一些基础设定
"""
from Config.routes import urls
import tornado.web
import os
from Config.settings import *
from Core.LogCore import Log

settings = {
    "template_path": os.path.join(os.getcwd(), "Templates"),
    "static_path": os.path.join(os.getcwd(), "Statics"),
    "debug": DEBUG,
    "autoreload": DEBUG,  # debug开启时,自动重载应用
    "compiled_template_cache": not DEBUG,  # debug开启时,关闭模版缓存
    "static_hash_cache": not DEBUG,  # debug开启时,关闭静态文件缓存
    "serve_traceback": DEBUG,  # debug开启时,当一个异常在 RequestHandler 中没有捕获，将会生成一个包含调用栈信息的错误页
    "logging": Log().set_logger_config_and_start(),  # 开启日志
}
# handlers指的是routes.py中的内容
application = tornado.web.Application(
    handlers=urls,
    **settings
)
