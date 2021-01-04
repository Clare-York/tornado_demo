# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 9:50
@Author      : chengyao
@File        : server.py
@introduce   :
"""
import tornado.ioloop
import tornado.httpserver
import tornado.options
from Core.applications import application
import sys
from Config.settings import HOST, PORT

# 定义一个变量，options.port = 8080。这样的好处是，
# 如果之后需要在tornado其他地方使用这个变量，
# 就可以直接用options.port就可以获得
tornado.options.define("port", default=PORT, help="run on this port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    # 根据application的设置，生成一个server
    http_server = tornado.httpserver.HTTPServer(application)
    # server调用监听方法，监听options.port端口
    # http_server.listen(tornado.options.options.port, address=HOST)

    http_server.bind(tornado.options.options.port, address=HOST)  # 多进程启动http_server，windows下不可用
    # 指定开启几个进程，默认值为1；
    # 如果参数num_processes为None或<=0，则自动根据机器硬件的cpu核芯数创建同等数目的子进程；如果参数值>0，则创建num_processes个子进程。
    http_server.start()

    lib = sys.path[0] + '\t' + HOST + '\t' + str(tornado.options.options.port)  # 为了打印现在server是来自哪个文件，以及在监听哪个端口
    print('Tornado server is running at %s' % lib)
    # 启动tornado服务
    tornado.ioloop.IOLoop.instance().start()
