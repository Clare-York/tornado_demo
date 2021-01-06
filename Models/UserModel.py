# coding: utf-8
"""
@Time        : 2021/1/6 15:32
@Author      : chengy_work@foxmail.com
@File        : UserModel.py
@Introduce   : 数据表users的实例化对象
"""
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from Models.BaseModel import Base
from datetime import datetime


class User(Base):
    """
    数据表users的实例化对象
    """
    __tablename__ = 'users'
    __table_args__ = {'comment': '???'}

    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(256, 'utf8mb4_general_ci'), nullable=False)
    telphone = Column(String(256, 'utf8mb4_general_ci'), nullable=False)
    status = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, default=datetime.now())
    deleted_at = Column(DateTime)

    def __repr__(self):
        return """{users:(id:%s, username:%s, telphone:%s, status:%s,created_at:%s, updated_at:%s,deleted_at:%s)}""" % (
            self.id, self.username, self.telphone, self.status, self.created_at, self.updated_at, self.deleted_at)


if __name__ == '__main__':
    Base.metadata.create_all()
