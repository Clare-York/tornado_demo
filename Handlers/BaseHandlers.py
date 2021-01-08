# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/8 9:48
@Author      : chengy_work@foxmail.com
@File        : BaseHandlers.py
@Introduce   :
"""
from Core.MysqlDriver import Database
from Core.RedisDriver import RedisDB


class BaseHandlers(object):
    """
    创建连接池
    """

    @property
    def db(self):
        """
        pass
        :return: session
        """
        return Database().session

    @property
    def redis(self):
        """
        pass
        :return: redis
        """
        return RedisDB().redis
