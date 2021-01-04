# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 10:17
@Author      : chengy_work@foxmail.com
@File        : TestHandlers.py
@Introduce   : 测试用
"""
from abc import ABC
from Config.log import logger, errlogger
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
        logger.debug("Remote_IP: %s" % self.request.remote_ip)
        logger.debug("Method: %s" % self.request.method)

        self.write("Headers: %s" % self.request.headers)  # 请求头

        self.write("<p></p>")

        self.write("Method: %s" % self.request.method)  # 请求方式

        self.write("<p></p>")

        self.write("Query: %s" % self.request.query)  # get请求?后拼接的内容

        self.write("<p></p>")

        self.write("Query_Arguments: %s" % self.request.query_arguments)  # get请求的参数

        self.write("<p></p>")

        self.write("Body: %s" % self.request.body)  # 请求体

        self.write("<p></p>")

        self.write("Body_Arguments: %s" % self.request.body_arguments)  # 请求体内的参数

        self.write("<p></p>")

        self.write("Arguments: %s" % self.request.arguments)  # 请求参数

        self.write("<p></p>")

        self.write("Files: %s" % self.request.files)  # 上传的文件

        self.write("<p></p>")

        self.write("Remote_IP: %s" % self.request.remote_ip)  # 来自IP

        self.write("<p></p>")

        self.write("Host: %s" % self.request.host)  # 服务运行地址

        self.write("<p></p>")

        self.write("Host_Name: %s" % self.request.host_name)  # 运行IP

        self.write("<p></p>")

        self.write("Uri: %s" % self.request.uri)  # 请求的路由+参数

        self.write("<p></p>")

        self.write("Path: %s" % self.request.path)  # 请求的具体路由

        self.write("<p></p>")

        self.write("Cookies: %s" % self.request.cookies)  # 未知

        self.write("<p></p>")

        self.write("Version: %s" % self.request.version)  # http协议版本

        self.write("<p></p>")

        self.write("Protocol: %s" % self.request.protocol)  # http/https协议

    def post(self):
        """
        处理post请求
        :return:
        """
        # 获取参数
        logger.debug("Remote_IP: %s" % self.request.remote_ip)
        logger.debug("Method: %s" % self.request.method)
        try:
            parameter_a = self.get_argument("a")
        except tornado.web.MissingArgumentError:
            errlogger.debug("Remote_IP: %s" % self.request.remote_ip)
            errlogger.debug("Method: %s" % self.request.method)
            errlogger.error("获取参数'a'失败！")
            # raise tornado.web.HTTPError(400)
        else:
            print("a:", parameter_a)

        # 获取上传的文件-单文件
        try:
            file_data = self.request.files["file"][0]
            filename = file_data["filename"]  # 文件名
            filebody = file_data["body"]  # 文件主体
            fileext = file_data["content_type"]  # 文件类型
        except KeyError:
            errlogger.debug("Remote_IP: %s" % self.request.remote_ip)
            errlogger.debug("Method: %s" % self.request.method)
            errlogger.error("获取参数失败")
            # raise tornado.web.HTTPError(401)
            # print("获取参数失败")
        except Exception as e:
            errlogger.debug("Remote_IP: %s" % self.request.remote_ip)
            errlogger.debug("Method: %s" % self.request.method)
            errlogger.error(e)
            # raise tornado.web.HTTPError(400)
            # print(e)
        else:
            if fileext.split('/')[0] == "image":  # 以图片为例
                f = open(filename, "wb")
                f.write(filebody)
                f.close()

        # 获取上传的文件-多文件
        try:
            file_ext = None
            file_name = None
            file_body = None
            file_data = self.request.files["file"][0]
            for file in file_data:
                file_name = file["filename"]
                file_body = file["body"]
                file_ext = file["content_type"]
        except KeyError:
            errlogger.debug("Remote_IP: %s" % self.request.remote_ip)
            errlogger.debug("Method: %s" % self.request.method)
            errlogger.error("获取参数失败")
            # raise tornado.web.HTTPError(401)
        except Exception as e:
            errlogger.debug("Remote_IP: %s" % self.request.remote_ip)
            errlogger.debug("Method: %s" % self.request.method)
            errlogger.error(e)
            # raise tornado.web.HTTPError(400)
        else:
            if file_ext.split('/')[0] == "image":  # 以图片为例
                file = open(file_name, 'wb')
                file.write(file_body)
                file.close()

        # 获取上传的图片-base64
        try:
            image_data = base64.b64decode(self.get_argument("image"))
        except KeyError:
            # raise tornado.web.HTTPError(401)
            errlogger.debug("Remote_IP: %s" % self.request.remote_ip)
            errlogger.debug("Method: %s" % self.request.method)
            errlogger.error("获取参数失败")
        except Exception as e:
            errlogger.debug("Remote_IP: %s" % self.request.remote_ip)
            errlogger.debug("Method: %s" % self.request.method)
            errlogger.error(e)
            # raise tornado.web.HTTPError(400)
        else:
            img = open("test.jpg", 'wb')
            img.write(image_data)
            img.close()

        # 获取json数据
        try:
            data = json.loads(self.request.body)
            parameter_a = data["a"]
        except json.decoder.JSONDecodeError:  # 不是json数据
            errlogger.debug("Remote_IP: %s" % self.request.remote_ip)
            errlogger.debug("Method: %s" % self.request.method)
            errlogger.error("不是Json数据")
            # raise tornado.web.HTTPError(403)
        except KeyError:  # 没有找到key
            errlogger.debug("Remote_IP: %s" % self.request.remote_ip)
            errlogger.debug("Method: %s" % self.request.method)
            errlogger.error("获取参数失败")
            # raise tornado.web.HTTPError(405)
        except Exception as e:
            errlogger.debug("Remote_IP: %s" % self.request.remote_ip)
            errlogger.debug("Method: %s" % self.request.method)
            errlogger.error(e)
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
