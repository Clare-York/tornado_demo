# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/11 9:49
@Author      : chengy_work@foxmail.com
@File        : SystemInfos.py
@Introduce   : 获取硬件使用信息
"""
import psutil
import time


class SystemInfo:
    """
    获取系统信息
    """

    def __init__(self):
        self.core = psutil.cpu_count()  # 核心数
        self.disk = psutil.disk_usage('/')  # 硬盘信息
        self.network = psutil.net_io_counters(pernic=True)
        self.key_name = "wlan0"
        # self.key_name = "WLAN 2"

    def _prepare(self):
        self.memory = psutil.virtual_memory()
        self.memory_total = round(self.memory.total / 1024 / 1024 / 1024, 2)  # 内存总大小 单位GB
        self.disk_total = round(self.disk.total / 1024 / 1024 / 1024, 2)  # 硬盘总大小 单位GB
        # self.keys = self.network.keys()
        self._get_rate()

    def _get_system_info(self):
        self._prepare()
        self.cpu_used = psutil.cpu_percent()
        self.memory_used = round(self.memory.used / self.memory.total * 100, 2)  # 内存用量 %
        self.disk_used = round(self.disk.used / self.disk.total * 100, 2)  # 硬盘用量 %

    def get_net_io(self):
        """
        获取网卡数据
        :return:
        """
        recv = psutil.net_io_counters(pernic=True).get(self.key_name).bytes_recv  # 指定网卡接收的字节数
        send = psutil.net_io_counters(pernic=True).get(self.key_name).bytes_sent  # 指定网卡发送的字节数
        return recv, send

    def _get_rate(self):
        old_recv, old_sent = self.get_net_io()  # 上一秒收集的数据
        time.sleep(1)
        now_recv, now_sent = self.get_net_io()  # 当前所收集的数据
        self.I = round((now_recv - old_recv) / 1024, 2)  # 每秒接收速率 K/s
        self.O = round((now_sent - old_sent) / 1024, 2)  # 每秒发送速率 K/s

    def main(self):
        """
        启动
        :return:
        """
        self._get_system_info()
        # print("\r%s核,\t %sG,\t %sG,\t CPU使用:%s%%,\t 内存使用:%s%%,\t 硬盘使用:%s%%,\t 实时上传:%sK/s,\t 实时下载:%sK/s" % (
        #     self.core, self.memory_total, self.disk_total, self.cpu_used, self.memory_used, self.disk_used,
        #     self.I, self.O), end="")
        # sys.stdout.flush()
        return self.core, self.memory_total, self.disk_total, self.cpu_used, self.memory_used, self.disk_used, self.I, self.O


if __name__ == '__main__':
    obj = SystemInfo()
    while 1:
        obj.main()
