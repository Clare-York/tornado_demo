# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/5 13:07
@Author      : chengy_work@foxmail.com
@File        : RedisDriver.py
@Introduce   : 创建redis连接池
"""
import redis
from Config.settings import REDIS_CONFIG
from loguru import logger


class RedisDB:
    """
    自定义Redis连接池
    """

    def __init__(self):
        self.db_config = REDIS_CONFIG
        self._create_pool()
        self.redis = self._get_connect()

    def _create_pool(self):
        """
        配置连接池
        :return:
        """
        if not self.db_config:
            logger.error("没有配置Redis信息")
            raise NameError
        try:
            self.pool = redis.ConnectionPool(decode_responses=True, **REDIS_CONFIG)
        except Exception as ex:
            logger.error("创建连接池失败!错误原因：%s" % ex)
        else:
            logger.success("创建Redis连接池成功")

    def _get_connect(self):
        """
        接入连接池
        :return: redis_cur
        """
        try:
            redis_cur = redis.StrictRedis(connection_pool=self.pool, decode_responses=True)
        except Exception as err:
            logger.error("无法接入连接池，请检查Redis配置,错误原因：%s" % err)
        else:
            logger.success("接入Redis连接池成功")
            return redis_cur
