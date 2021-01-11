# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/8 16:16
@Author      : chengy_work@foxmail.com
@File        : PushCore.py
@Introduce   : 用于向client端推送消息
"""
from uuid import uuid4
from loguru import logger

connector = dict()  # 记录当前连接的user


class PushCore:
    """
    用户控制及推送
    """

    @staticmethod
    def user_connect(user):
        """
        pass
        :param user:
        :return:
        """
        if user not in connector:
            uuid = str(uuid4())
            connector.setdefault(uuid, user)
            logger.debug("用户：%s,加入连接" % connector.get(uuid))
            return uuid

    @staticmethod
    def user_remove(uuid):
        """
        pass
        :param uuid:
        :return:
        """
        logger.debug("用户：%s,断开连接" % uuid)
        try:
            del connector[uuid]
        except Exception as e:
            logger.error(e)
        else:
            logger.success("成功清理用户：%s连接信息" % uuid)

    @staticmethod
    def trigger(message, uuid=None):
        """
        向已被记录的客户端推送最新内容
        :param uuid:
        :param message:
        :return:
        """
        logger.debug("即将开始推送...")
        if not connector:
            logger.warning("无连接用户，不执行推送...")
            return
        if uuid is None:
            # 推送给所有client
            for uuid, user in connector.items():
                logger.debug("开始向用户：%s,推送：%s" % (user, message))
                try:
                    user.write_message(message)
                except Exception as e:
                    logger.error(e)
                logger.success("向用户：%s,推送成功" % user)
        else:
            # 推送给指定client
            user = connector.get(uuid)
            try:
                user.write_message(message)
            except Exception as e:
                logger.error(e)
            logger.success("向用户：%s,推送成功" % user)
