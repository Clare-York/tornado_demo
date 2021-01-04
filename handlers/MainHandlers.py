# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 9:55
@Author      : chengyao
@File        : MainHandlers.py
@introduce   : 根路由对应的执行逻辑-模版
"""
from abc import ABC

import tornado.web
import json
import os
import base64


# 注意url中import的MainHandler名字，必须跟这里handler的名字一样
class MainHandler(tornado.web.RequestHandler, ABC):
    """
    用get的方式访问这个handler的话，就进入到get方法。
    这里没有写post的方法，如果用post的方法进入到这个handler会报错
    """

    def get(self):
        """
        处理get请求
        :return:
        """
        print(self.request.headers)  # 打印请求头
        print(self.request.method)  # 打印请求方式

        print(self.request.query)  # 打印query参数
        print(self.request.query_arguments)  # 打印query参数

        print(self.request.body)  # 打印请求体
        print(self.request.body_arguments)  # 打印body参数

        print(self.request.arguments)  # 打印请求参数
        print(self.request.files)  # 打印文件信息

        print(self.request.remote_ip)  # 打印请求来自IP
        print(self.request.host_name)  # 打印IP

        print(self.request.uri)  # 打印请求具体路由
        print(self.request.path)  # 打印来自哪个目录

        print(self.request.connection)  # 打印连接哪个http_server
        print(self.request.server_connection)  # 打印连接哪个http_server

        print(self.request.version)  # 打印http_version
        print(self.request.protocol)  # 打印连接协议
        # write方法是打印到浏览器。若想打开一个html文件之类的，就需要用render
        self.write('hello word')

    def post(self):
        """
        处理post请求
        :return:
        """
        # 获取参数
        # try:
        #     parameter_a = self.get_argument("a")
        # except tornado.web.MissingArgumentError:
        #     raise tornado.web.HTTPError(403)
        # else:
        #     print("a:", parameter_a)

        # 获取上传的文件-单文件
        # file_data = self.request.files["file"][0]
        # filename = file_data["filename"]  # 文件名
        # filebody = file_data["body"]  # 文件主体
        # fileext = file_data["content_type"]  # 文件类型
        # if fileext.split('/')[0] == "image":  # 以图片为例
        #     file = open(filename, "wb")
        #     file.write(filebody)
        #     file.close()

        # 获取上传的文件-多文件
        # file_data = self.request.files["file"][0]
        # for file in file_data:
        #     filename = file["filename"]
        #     filebody = file["body"]
        #     fileext = file["content_type"]
        #     if fileext.split('/')[0] == "image":  # 以图片为例
        #         file = open(filename, 'wb')
        #         file.write(filebody)
        #         file.close()

        # 获取上传的图片-base64
        # data = self.get_argument("image")
        # image_data = base64.b64decode(data)
        # f = open("test.jpg", 'wb')
        # f.write(image_data)
        # f.close()

        # 获取json数据
        try:
            data = json.loads(self.request.body)
            parameter_a = data["a"]
        except json.decoder.JSONDecodeError:  # 不是json数据
            raise tornado.web.HTTPError(403)
        except KeyError:  # 没有找到key
            raise tornado.web.HTTPError(405)
        else:
            print("a:", parameter_a)
