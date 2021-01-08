# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/6 16:34
@Author      : chengy_work@foxmail.com
@File        : BaseModel.py
@Introduce   : 模型基类，用于实例化数据表
"""
from Core.MysqlDriver import Database
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(Database().engine)
db = Database().session
