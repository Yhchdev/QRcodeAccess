# coding: utf-8
from sqlalchemy import *
from sqlalchemy import CHAR, Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session

# 数据库的连接配置
from configs import DB_URI

Base = declarative_base()

# 数据库引擎
engin = create_engine(DB_URI)

metadata = Base.metadata


# 创建事务

session = create_session(bind=engin)


class AccessInfo(Base):
    __tablename__ = 'access_info'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False)
    sex = Column(CHAR(2), nullable=False)
    phone = Column(String(255), nullable=False)
    id_card = Column(String(255), nullable=False)
    idcard_sha256 = Column(String(255), nullable=False)
    address = Column(String(1000))
    people_num = Column(INTEGER(5))
    plate_num = Column(String(255))
    cause = Column(String(2000), nullable=False)
    carry = Column(String(1000))
    time_start = Column(String(255), nullable=False)
    tiem_end = Column(String(255), nullable=False)
    respondent_name = Column(String(255), nullable=False)
    respondent_dept = Column(String(255), nullable=False)

    # 插入数据
    def insertOne(self,access_new):
        session.add(access_new)
        session.commit()
        session.close()

    # 根据加密后的 身份证信息 查询单个对象
    def queryObject(self,idcard_sha256):
        accessInfo= session.query(AccessInfo).filter(AccessInfo.idcard_sha256).first()
        return accessInfo