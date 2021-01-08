# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/8 11:02
@Author      : chengy_work@foxmail.com
@File        : BaseHandlers.py
@Introduce   :
"""
from Models.BaseModel import database
from Core.RedisDriver import RedisDB


class BaseHandler(object):
    """
    定义连接池
    """

    @property
    def db(self):
        """
        pass
        :return: session
        """
        return database.session

    @property
    def redis(self):
        """
        pass
        :return: redis
        """
        return RedisDB().redis
