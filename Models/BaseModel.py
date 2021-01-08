# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/6 16:34
@Author      : chengy_work@foxmail.com
@File        : BaseModel.py
@Introduce   : 模型基类，用于实例化数据表
"""
from Core.MysqlDriver import database
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import BigInteger, Column, DateTime, func

Base = declarative_base(database.engine)


class BaseModel(object):
    """
    创建所有模型基类
    """

    @declared_attr
    def id(self):
        """
        所有模型（表）的共有字段
        :return:
        """
        return Column(BigInteger, primary_key=True, index=True)

    @declared_attr
    def created_at(self):
        """
        所有模型（表）的共有字段
        :return:
        """
        return Column(DateTime, default=func.now())

    @declared_attr
    def updated_at(self):
        """
        所有模型（表）的共有字段
        :return:
        """
        return Column(DateTime, default=func.now())

    @declared_attr
    def deleted_at(self):
        """
        所有模型（表）的共有字段
        :return:
        """
        return Column(DateTime)

    @declared_attr
    def query(self):
        """
        为模型创建query
        :return:
        """
        return database.session.query_property()  # 创建query
