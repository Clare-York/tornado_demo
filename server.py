# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 9:50
@Author      : chengy_work@foxmail.com
@File        : server.py
@Introduce   : tornado服务主程序
"""
import tornado.ioloop
import tornado.httpserver
import tornado.options
from Core.Applications import application
import sys
from Config.configs import HOST, PORT
from Config.log import logger

# 定义一个变量，options.port = 8080。
# 这样的好处是，如果之后需要在其他地方使用这个变量，就可以直接用options.port就可以获得

tornado.options.define("port", default=PORT, help="run on this port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()  # 加入此行可在运行时利用命令行--port xxx 指定运行端口

    http_server = tornado.httpserver.HTTPServer(application)  # 根据application的设置，生成一个http_server

    # http_server.listen(tornado.options.options.port, address=HOST)  # 运行在address上，监听options.port端口

    http_server.bind(tornado.options.options.port, address=HOST)  # 多进程启动http_server，windows下不可用

    http_server.start()  # 默认num_processes=1，当值<=0或None则自动根据cpu核芯数创建同等数目的子进程,>0则创建指定的子进程

    lib = sys.path[0] + '\t' + HOST + '\t' + str(tornado.options.options.port)  # 为了打印现在server是来自哪个文件，以及在监听哪个端口
    logger.debug('Tornado server is running at %s' % lib)

    tornado.ioloop.IOLoop.instance().start()  # 启动tornado服务
