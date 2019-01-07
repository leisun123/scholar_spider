# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: withdraw.py

@time: 1/7/19 17:04


'''


##将数据库中信息导出到excal文档


from db.operateSql import session
from db.operateSql import People
import csv


datas = session.query(People.name, People.email, People.major, People.web, People.orginazation).all()

with open('new2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'email', 'major', 'web', 'organization'])
    for row in datas:
        writer.writerow(row)