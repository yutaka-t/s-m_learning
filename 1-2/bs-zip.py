#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request as req

from bs4 import BeautifulSoup

url = "http://api.aoikujira.com/zip/xml/1500042"

# 参考：URLにアクセスした際の結果
rei = """
    <address result="1">
    <header>
    <result>1</result>
    <api>api.aoikujira.com/zip</api>
    <version>1.1</version>
    </header>
    <value>
    <zip>1500042</zip>
    <ken>東京都</ken>
    <shi>渋谷区</shi>
    <cho>宇田川町</cho>
    <disp>東京都渋谷区宇田川町</disp>
    <kenkana>トウキョウト</kenkana>
    <shikana>シブヤク</shikana>
    <chokana>ウダガワチョウ</chokana>
    </value>
    </address>
"""

# urlopen() でデータを取得
res = req.urlopen(url)

# BeautifulSoupで解析
soup = BeautifulSoup(res, "html.parser")

# 任意のデータを抽出
ken = soup.find("ken").string
shi = soup.find("shi").string
cho = soup.find("cho").string
disp = soup.find("disp").string
print(ken, shi, cho, disp)
