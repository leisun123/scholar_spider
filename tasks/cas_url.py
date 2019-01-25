# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: cas_url.py

@time: 1/25/19 10:50


'''

from db.operateSql import db_url, connect_db, Info
from utils.connection import *

session = connect_db(db_url)
print(db_url)


def get_info(url):
    res = fetch(url)
    tmp = extract("//div[@class='Contentbox']//td[@class='zh12']", res, True)
    for i in tmp:
        each = str(etree.tostring(i))
        name = extract('//a/text()', each)
        if '*' in str(name):
            name = name.replace('*', '')
        fullurl = extract('//a/@href', each)
        if fullurl and 'www.' in fullurl:
            mainurl = fullurl.split('www.')[1].replace('/', '')
        elif fullurl and 'www.' not in fullurl:
            mainurl = fullurl.split('http://')[1].replace('/', '')
        else:
            continue
        print(name, fullurl, mainurl)
        infos = Info(name=name, fullurl=fullurl, mainurl=mainurl)
        session.add(infos)
        try:
            session.commit()
        except Exception as e:
            print(e)
            session.rollback()


get_info("http://www.cas.cn/jg/ysjg/yzssydw/")
get_info("http://www.cas.cn/jg/ysjg/xxjggzcdw/")
get_info("http://www.cas.cn/jg/ysjg/nzzyzssydw/")
get_info("http://www.cas.cn/jg/ysjg/gjdw/")
get_info("http://www.cas.cn/jg/ysjg/kgqy/")
get_info("http://www.cas.cn/jg/ysjg/other/")