# -*- coding: utf-8 -*-
"""
@Time        : 2021/1/4 9:53
@Author      : chengyao
@File        : routes.py
@introduce   :
"""
# 找到对应的handler位置，并import

from handlers.MainHandlers import MainHandler
from handlers.ArticleHandlers import ArticleHandler

# 存入到列表中，后续注册到server端，告诉server端不同地址，
# 应该找不同的handler，其中“/”代表的是根网站，例如：x.x.com.
# 若“/app”，则访问x.x.com/app可以访问对应的资源
url = [
    (r"/", MainHandler),  # 根路由
    (r"/a", ArticleHandler),

]
