# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 13:00
@Author      : chengy_work@foxmail.com
@File        : settings_example.py
@Introduce   : 配置文件模板，使用时需将文件重命名为settings.py,并填入对应内容
"""
# 调试开关（True pr False）,默认为True,若在生成环境运行请改为False
DEBUG = True

# 运行IP，默认为127.0.0.1，需外部访问，建议使用nginx反向代理，或将HOST修改为“0.0.0.0”（不推荐）
HOST = "127.0.0.1"

# 监听端口
PORT = 8080

# MySQ数据库配置
MYSQL_CONFIG = {
    "host": "127.0.0.1",  # 地址,默认 127.0.0.1
    "port": 3306,  # 端口,默认 3306
    "db": "",  # 数据库名
    "user": "",  # 用户名
    "password": ""  # 密码
}

# Redis数据库配置
REDIS_CONFIG = {
    "host": "127.0.0.1",  # 地址,默认 127.0.0.1
    "port": 6379,  # 端口,默认 6379
    "db": 0,  # 指定db，默认 0
    "password": "",  # 密码,默认 空
}
