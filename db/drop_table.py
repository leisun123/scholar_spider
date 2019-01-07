# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: drop_table.py

@time: 1/7/19 17:13


'''

##删除数据表

from sqlalchemy import create_engine

from db.operateSql import Base, db_url

Base.metadata.drop_all(create_engine(db_url, encoding="UTF-8"))
