#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request as req

from bs4 import BeautifulSoup

url = "http://stocks.finance.yahoo.co.jp/stocks/detail/?code=usdjpy"


def html_parser(p_url):
    """
    HTMLを解析する
    :param p_url:解析するURL
    :return: 解析結果
    """
    res = req.urlopen(p_url)
    return BeautifulSoup(res, "html.parser")


# HTML解析
soup = html_parser(url)

# 任意のデータを抽出
price = soup.select_one(".stoksPrice").string
print("usd/jpy=", price)
