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
from Core.RedisDriver import RedisDB
from Core.MysqlDriver import Session
from Models.TestModel import User


class TestHandler(tornado.web.RequestHandler, ABC):
    """
    测试用
    """

    def __init__(self, *args, **kwargs):
        super(TestHandler, self).__init__(*args, **kwargs)
        self.redis = RedisDB().redis
        self.db = Session

    def get(self):
        """
        处理get请求，查
        :return:
        """
        logger.debug("Remote_IP: %s,Method: %s" % (self.request.remote_ip, self.request.method))
        sql = "SELECT VERSION()"
        redis_re = self.redis.get("name")
        result = User.query.filter(User.username == 'asd').all()
        resul2 = self.db.query(User.id).filter(User.username == 'asd').first()
        result3 = self.db.execute(sql).fetchone()  # 原生SQL
        self.db.remove()  # 释放连接
        self.write("redis: %s " % redis_re)
        self.write("query:%s,\n query():%s,\n execute()%s" % (result, resul2, result3))

    def post(self):
        """
        处理post请求，增
        :return:
        """
        logger.debug("Remote_IP: %s,Method: %s" % (self.request.remote_ip, self.request.method))
        name = self.request.body_arguments.get('name')[0]
        tel = self.request.body_arguments.get('phone')[0]
        user = User(username=str(name), telphone=str(tel), created_at=datetime.now())
        try:
            self.db.add(user)
            self.db.commit()
        except Exception as e:
            logger.error(e)
            self.db.rollback()
            self.set_status(500)
        else:
            self.db.remove()
            self.write("新增成功")

    def put(self):
        """
        处理put请求,改
        :return:
        """
        logger.debug("Remote_IP: %s,Method: %s" % (self.request.remote_ip, self.request.method))
        name = self.request.body_arguments.get('name')[0]
        user_id = self.request.body_arguments.get('id')[0]
        try:
            self.db.update(User.username == str(name)).filter_by(User.id == user_id).first()
            self.db.commit()
        except Exception as e:
            logger.error(e)
            self.db.rollback()
            self.set_status(500)
        else:
            self.db.remove()  # 释放连接
            self.write("修改成功")

    def delete(self):
        """
        处理delete请求，删
        :return:
        """
        logger.debug("Remote_IP: %s,Method: %s" % (self.request.remote_ip, self.request.method))
        name = self.request.body_arguments.get('name')[0]
        user_id = self.request.body_arguments.get('id')[0]
        try:
            self.db.update(User.status == 0, User.deleted_at == datetime.now()).filter_by(
                User.id == user_id).first()  # 逻辑删除
            User.query.filter_by(User.id == user_id).delete()
            self.db.commit()
        except Exception as e:
            logger.error(e)
            self.db.rollback()
            self.set_status(500)
        else:
            self.db.remove()  # 释放连接
            self.write("修改成功")

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
