# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/5 11:09
@Author      : chengy_work@foxmail.com
@File        : MysqlDriver.py
@Introduce   : 创建mysql连接池
"""
import MySQLdb
# from dbutils.pooled_db import PooledDB
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
        self.db = self._get_connect()

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

            # 原生连接池创建
            # self.Pool = PooledDB(creator=MySQLdb,  # 使用链接数据库的模块
            #                      mincached=2,  # 连接池允许的最大连接数，0和None表示不限制连接数
            #                      maxcached=5,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            #                      maxshared=3,  # 链接池中最多闲置的链接，0和None不限制
            #                      maxconnections=6,  # 链接池中最多共享的链接数量，0和None表示全部共享
            #                      blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            #                      charset="utf8",
            #                      **self._db_config)
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
        Session = sessionmaker(bind=self.engine)  # 创建Session工厂
        # session = Session()
        session = scoped_session(Session)  # 通过 registry 模式 协助管理session (多线程安全)
        return session
