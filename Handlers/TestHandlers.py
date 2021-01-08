# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 10:17
@Author      : chengy_work@foxmail.com
@File        : TestHandlers.py
@Introduce   : 测试用
"""
from abc import ABC
from loguru import logger
import tornado.web
from datetime import datetime
from Handlers.BaseHandlers import BaseHandler
from Models.TestModel import User


class TestHandler(tornado.web.RequestHandler, BaseHandler, ABC):
    """
    测试用
    """

    def get(self):
        """
        处理get请求，查
        :return:
        """
        logger.debug("Remote_IP: %s,Method: %s" % (self.request.remote_ip, self.request.method))
        sql = "SELECT VERSION()"
        name = self.get_query_argument("name")
        redis_re = self.redis.get("name")
        result = User.query.filter(User.username == name).all()[0]
        resul2 = self.db.query(User.id).filter(User.username == name).first()[0]
        result3 = self.db.execute(sql).fetchone()[0]  # 原生SQL
        self.db.remove()  # 释放连接
        self.write("redis: %s \n" % redis_re)
        self.write("query:%s,\n query():%s,\n execute()%s" % (result, resul2, result3))

    def post(self):
        """
        处理post请求，增
        :return:
        """
        logger.debug("Remote_IP: %s,Method: %s" % (self.request.remote_ip, self.request.method))
        name = self.get_body_argument('name')
        tel = self.get_body_argument('phone')
        user = User(username=str(name), telphone=str(tel))
        try:
            self.db.add(user)
            self.db.commit()
        except Exception as e:
            logger.error(e)
            self.db.rollback()
            self.set_status(500)
        else:
            self.db.remove()
            result = User.query.filter(User.username == name).all()[0]
            self.write("新增成功 \n %s" % result)

    def put(self):
        """
        处理put请求,改
        :return:
        """
        logger.debug("Remote_IP: %s,Method: %s" % (self.request.remote_ip, self.request.method))
        name = self.get_body_argument('name')
        user_id = self.get_body_argument('id')
        try:
            User.query.filter(User.id == user_id).update({User.username: str(name), User.updated_at: datetime.now()})
            self.db.commit()
        except Exception as e:
            logger.error(e)
            self.db.rollback()
            self.set_status(500)
        else:
            result = User.query.filter(User.id == user_id).all()[0]
            self.db.remove()  # 释放连接
            self.write("修改成功\n %s" % result)

    def delete(self):
        """
        处理delete请求，删
        :return:
        """
        logger.debug("Remote_IP: %s,Method: %s" % (self.request.remote_ip, self.request.method))
        user_id = self.request.body_arguments.get('id')[0]
        try:
            User.query.filter(User.id == user_id).update({User.status: 0, User.deleted_at: datetime.now()})  # 逻辑删除
            # User.query.filter(User.id == user_id).delete()  # 实际删除
            self.db.commit()
        except Exception as e:
            logger.error(e)
            self.db.rollback()
            self.set_status(500)
        else:
            result = User.query.filter(User.status == 1).all()
            self.db.remove()  # 释放连接
            self.write("删除成功\n %s" % result)

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
