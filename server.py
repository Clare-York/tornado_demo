# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 9:50
@Author      : chengy_work@foxmail.com
@File        : server.py
@Introduce   : tornado服务主程序
"""
import tornado.ioloop
import sys
from Core.Applications import application
from Config.settings import HOST, PORT, DEBUG
from loguru import logger
from tornado import httpserver
from tornado.options import options, define, parse_command_line

# 定义一个变量，options.port = 8080。
# 这样的好处是，如果之后需要在其他地方使用这个变量，就可以直接用options.port就可以获得
define("port", default=PORT, help="run on this port", type=int)
# 定义一个变量，options.host = '127.0.0.1'
define("host", default=HOST, help="run on this host", type=str)

if __name__ == "__main__":
    parse_command_line()  # 加入此行可在运行时利用命令行--port xxx --host 'xxx.x.x.x'指定运行地址和端口

    http_server = httpserver.HTTPServer(application)  # 根据application的设置，生成一个http_server

    if DEBUG:
        http_server.listen(options.port, address=options.host)  # 运行在address上，监听options.port端口
    else:
        http_server.bind(options.port, address=options.host)  # 多进程启动http_server，windows下不可用
        http_server.start(num_processes=-1)  # 默认为1，当值<=0则自动根据cpu核芯数创建同等数目的子进程,>0则创建指定的子进程

    lib = sys.path[0] + '\t' + options.host + '\t' + str(options.port)  # 为了打印现在server是来自哪个文件，以及在监听哪个端口
    logger.debug("Tornado server is running at %s" % lib)

    tornado.ioloop.IOLoop.instance().start()  # 启动tornado服务
