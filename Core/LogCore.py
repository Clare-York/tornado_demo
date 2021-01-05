# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 21:09
@Author      : chengy_work@foxmail.com
@File        : LogCore.py
@Introduce   : 日志模块
"""
from loguru import logger
import os


class Log:
    """
    日志模块核心功能
    """

    def __init__(self):
        self._logging_path = os.path.join(os.getcwd(), "logs")
        self._log_name = "Runtime_{time:YYYY-MM-DD}.log"

    def set_logger_config_and_start(self):
        """
        配置log输出、分割、压缩等
        :return:
        """
        if not os.path.exists(self._logging_path):
            os.mkdir(self._logging_path)
        logger.add(os.path.join(self._logging_path, self._log_name), rotation="00:00", retention="30 days",
                   level="DEBUG",
                   encoding='utf-8')  # 每天0点整分割一次日志，最长保留30天
