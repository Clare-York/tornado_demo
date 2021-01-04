# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 22:10
@Author      : chengy_work@foxmail.com
@File        : log.py
@Introduce   : 配置文件
"""
from Core.LogCore import Log
from Config.configs import LOG

if LOG:
    logger = Log().getlogger()[0]
    errlogger = Log().getlogger()[1]
else:
    logger = Log().getlogger()[0].remove()
    errlogger = Log().getlogger()[1].remove()
