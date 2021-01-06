# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/5 11:09
@Author      : chengy_work@foxmail.com
@File        : MysqlDriver.py
@Introduce   : 创建mysql连接池
"""
import MySQLdb
from Config.settings import MYSQL_CONFIG
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class Database:
    """
    自定义mysql连接池
    """

    def __init__(self):
        self._db_config = MYSQL_CONFIG
        self._db_url = "mysql+mysqldb://{user}:{password}@{host}:{port}/{db}?charset=utf8"
        self._create_pool()
        self._get_connect()

    def _create_pool(self):
        """
        创建连接池
        :return:
        """
        if not self._db_config:
            logger.error("没有配置MySQL数据库信息")
            raise NameError
        try:
            # ORM自带连接池
            self.engine = create_engine(self._db_url.format(**self._db_config))  # 创建连接池
        except MySQLdb.OperationalError:
            logger.error("创建MySQL连接池失败!")
        except Exception as e:
            logger.error("创建MySQL连接池失败!错误原因%s" % e)
        else:
            logger.success("创建MySQL连接池成功")

    def _get_connect(self):
        """
        与mysql建立连接
        :return:conn,cur
        """
        session_factory = sessionmaker(bind=self.engine)  # 创建Session工厂
        self.session = scoped_session(session_factory)  # 通过 registry 模式 协助管理session (多线程安全)


Session = Database().session
