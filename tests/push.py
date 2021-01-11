# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/11 13:50
@Author      : chengy_work@foxmail.com
@File        : push.py
@Introduce   : 执行推送逻辑
"""
import requests
from SystemInfos import SystemInfo
from loguru import logger
import time

systeminfo = SystemInfo()
url = "http://127.0.0.1:8000/receive"


def push():
    """
    pss
    """
    while True:
        try:
            core, memory_total, disk_total, cpu_used, memory_used, disk_used, I, O = systeminfo.main()
            message = {"core": core, "memory_total": memory_total, "disk_total": disk_total, "cpu_used": cpu_used,
                       "memory_used": memory_used, "disk_used": disk_used, "network_input": I, "network_output": O}
        #     print(message)
        # except Exception as e:
        #     print(e)
        #     return
            logger.debug(message)
            response = requests.post(url, data=message)
        except Exception as e:
            logger.error(e)
            break
        else:
            # logger.success("%s,本轮推送成功" % response)
            time.sleep(5)


if __name__ == '__main__':
    push()
