# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 10:17
@Author      : chengyao
@File        : TestHandlers.py
@introduce   :测试用
"""
from abc import ABC
import tornado.web
import json
import base64


class TestHandler(tornado.web.RequestHandler, ABC):
    """
    测试用
    """

    def get(self):
        """
        处理get请求
        :return:
        """
        self.write("Headers: %s" % self.request.headers)
        self.write("Method: %s" % self.request.method)
        self.write("Query: %s" % self.request.query)
        self.write("Query_Arguments: %s" % self.request.query_arguments)
        self.write("Body: %s" % self.request.body)
        self.write("Body_Arguments: %s" % self.request.body_arguments)
        self.write("Arguments: %s" % self.request.arguments)
        self.write("Files: %s" % self.request.files)
        self.write("Remote_IP: %s" % self.request.remote_ip)
        self.write("Host: %s" % self.request.host)
        self.write("Host_Name: %s" % self.request.host_name)
        self.write("Uri: %s" % self.request.uri)
        self.write("Path: %s" % self.request.path)
        self.write("Connection: %s" % str(self.request.connection))
        self.write("Server_Connection: %s" % str(self.request.server_connection))
        self.write("Version: %s" % self.request.version)
        self.write("Protocol: %s" % self.request.protocol)

    def post(self):
        """
        处理post请求
        :return:
        """
        # 获取参数
        try:
            parameter_a = self.get_argument("a")
        except tornado.web.MissingArgumentError:
            raise tornado.web.HTTPError(400)
        else:
            print("a:", parameter_a)

        # 获取上传的文件-单文件
        try:
            file_data = self.request.files["file"][0]
            filename = file_data["filename"]  # 文件名
            filebody = file_data["body"]  # 文件主体
            fileext = file_data["content_type"]  # 文件类型
        except Exception:
            raise tornado.web.HTTPError(400)
        else:
            if fileext.split('/')[0] == "image":  # 以图片为例
                file = open(filename, "wb")
                file.write(filebody)
                file.close()

        # 获取上传的文件-多文件
        try:
            file_data = self.request.files["file"][0]
            for file in file_data:
                filename = file["filename"]
                filebody = file["body"]
                fileext = file["content_type"]
        except Exception:
            raise tornado.web.HTTPError(400)
        else:
            if fileext.split('/')[0] == "image":  # 以图片为例
                file = open(filename, 'wb')
                file.write(filebody)
                file.close()

        # 获取上传的图片-base64
        try:
            img_data = self.get_argument("image")
            image_data = base64.b64decode(img_data)
        except Exception:
            raise tornado.web.HTTPError(400)
        else:
            f = open("test.jpg", 'wb')
            f.write(image_data)
            f.close()

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

    def put(self):
        """
        处理put请求
        :return:
        """
        pass

    def delete(self):
        """
        处理delete请求
        :return:
        """
        pass

    def head(self):
        """
        处理head请求
        :return:
        """
        pass

    def options(self):
        """
        处理options请求
        :return:
        """
        pass

    def patch(self):
        """
        处理patch请求
        :return:
        """
        pass
