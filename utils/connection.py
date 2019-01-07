# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: connection.py

@time: 1/7/19 17:07


'''

import time

import requests
from lxml import etree

from config import proxies
from ErrorHandle.request_error import HTTPError, URLFetchError
from config import USER_AGENT


def fetch(url, requests_session=requests.Session(),
          timeout=10,
          from_web=True,
          retry_num=5,
          Proxies=None,
          logger=None,
          decode=True):
    if not from_web:
        with open('', 'rb') as f:
            return f.read()
    else:
        kwargs = {
            "headers": {
                "User-Agent": USER_AGENT,
            }
        }
        kwargs["timeout"] = timeout
        resp = None
        for i in range(retry_num):
            try:
                # 是否启动代理
                if Proxies is not None:
                    kwargs["proxies"] = {
                        "http": "", \
                        "https": ""
                    }
                resp = requests_session.get(url, **kwargs)
                time.sleep(2)
                if resp.status_code != 200:
                    raise HTTPError(resp.status_code, url)
                break
            except Exception as exc:
                logger.warn("%s %d failed!\n%s", url, i, str(exc))

                continue
        if resp is None:
            raise URLFetchError(url)
        if decode:
            return resp.content.decode("UTF8")
        else:
            return resp.content


def extract(regx, html_source, multi=False):
    # lxml解析
    if isinstance(html_source, str):
        html_source = etree.HTML(html_source)
    res = html_source.xpath(regx)
    if multi:
        return res
    return res[0] if res else None