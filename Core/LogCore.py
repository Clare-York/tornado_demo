# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 21:09
@Author      : chengy_work@foxmail.com
@File        : LogCore.py
@Introduce   : 配置文件
"""
import loguru
import os


class Log:
    def __init__(self):
        self.logger = loguru.logger
        self.errlogger = loguru.logger
        self.logging_path = os.path.join(os.getcwd(), "logs")
        self.log_name = "Runtime_{time:YYYY-MM-DD}.log"
        self.errlog_name = "Error_{time:YYYY-MM-DD}.log"

    def set_logger_config(self):
        """
        配置log输出
        :return:
        """
        if not os.path.exists(self.logging_path):
            os.mkdir(self.logging_path)
        self.logger.add(os.path.join(self.logging_path, self.log_name), rotation="00:00", retention="30 days",
                        level="DEBUG",
                        encoding='utf-8')  # 每天0点整分割一次日志，最长保留30天
        self.errlogger.add(os.path.join(self.logging_path, self.errlog_name), rotation="00:00", retention="30 days",
                           level="DEBUG",
                           encoding='utf-8')  # 每天0点整分割一次日志，最长保留30天

    def getlogger(self):
        """
        配置并返回logger实例
        :return:
        """
        self.set_logger_config()
        return self.logger, self.errlogger
