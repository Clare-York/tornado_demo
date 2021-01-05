# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 13:00
@Author      : chengy_work@foxmail.com
@File        : settings_template.py
@Introduce   : 配置文件模板，使用时需将文件重命名为settings.py,并填入对应内容
"""
# 调试开关（True pr False）,默认为True
DEBUG = True

# 运行IP，默认为127.0.0.1，需外部访问，建议使用nginx反向代理，或将HOST修改为“0.0.0.0”（不推荐）
HOST = "127.0.0.1"

# 监听端口
PORT = 8080
