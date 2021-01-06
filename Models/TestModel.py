# coding: utf-8
"""
@Time        : 2021/1/6 15:32
@Author      : chengy_work@foxmail.com
@File        : TestModel.py
@Introduce   : 数据表users的实例化对象
"""
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from Models.BaseModel import Base
from datetime import datetime


class User(Base):
    """
    数据表users的实例化对象
    Column的常用参数：
        default: 默认值，可以传一个函数体，default的值等于这个函数体执行后返回的值
        nullable：是否可为空
        primary_key：是否为主键
        unique: 是否唯一
        autoincrement： 是否自增长
        onupdate: 更新的时候执行的函数，和default一样，可以传一个函数体
        name: 该属性在数据库中的字段的映射，默认是属性名
    常用的数据类型
        Integer: 整形
        Float: 浮点类型
        Boolean：布尔
        DECIMAL: 定点类型： DECIMAL第一个参数为整数位的个数，第二位参数为小数位的个数
        Enum：枚举类型： Enum可以借助python3自带的enum包来实现更加简便
        Date: 传递datetime.date()
        DateTime: 传递datetime.datetime()
        Time：传递datetime.time()
        String: 字符串型, 使用时需要制定长度
        Text: 文本类型
        LONGTEXT: 长文本类型
    """
    __tablename__ = 'users'
    __table_args__ = {'comment': '???'}

    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(256, 'utf8mb4_general_ci'), nullable=False)
    telphone = Column(String(256, 'utf8mb4_general_ci'), nullable=False)
    status = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.now())
    deleted_at = Column(DateTime)

    def __repr__(self):
        """
        提供查询时显示的内容
        :return:
        """
        return """{users:(id:%s, username:%s, telphone:%s, status:%s,created_at:%s, updated_at:%s,deleted_at:%s)}""" % (
            self.id, self.username, self.telphone, self.status, self.created_at, self.updated_at, self.deleted_at)


if __name__ == '__main__':
    # 使用Base类在数据库内创建表格，只能新建，不能更新
    # 若已提前建好数据表，可使用以下命令将数据表实例为本文件
    # sqlacodegen --tables <table_name> "mysql://<user>:<passwd>@<host>:<port>/<db_name>"><Table_nameModel.py>
    Base.metadata.create_all()
