# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 10:17
@Author      : chengyao
@File        : ArticleHandlers.py
@introduce   :
"""
from abc import ABC
import tornado.web
import sys
import os


class ArticleHandler(tornado.web.RequestHandler, ABC):
    """
    pass
    """

    def get(self):
        """
        pass
        :return:
        """
        if "num" and "name" in self.request.uri:
            article_name = self.get_argument("name")
            article_num = self.get_argument("num")
            # 把参数组装成文件地址
            print(sys.path[0])
            filename = sys.path[0] + u'/article/%s/第%s章.txt' % (article_name, article_num)

            # 检查文件是否存在，不存在则报文件不存在错误
            if os.path.isfile(filename):
                result = ''
                # 打开对应文件，用只读的方式
                with open(filename, encoding="utf-8") as f:
                    # 遍历获得的文件内容，并拼接成正确的字符串输出
                    for line in f.readlines():
                        # 去除'\n'的换行符，并且替换成html的换行标签
                        line = line.strip()
                        if line and line != ' ':
                            result = result + '<br><br>' + line
                # 输出到网页
                self.write(result)
            else:
                self.write('file does not exsit')

        else:
            self.write('missing parameter')
