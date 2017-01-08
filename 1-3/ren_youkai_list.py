#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request as req

from bs4 import BeautifulSoup

url = "http://www.xn--gcki3eh5182c5sam28axq7b3ig.com/yokai_medal_list/"

# urlopen() でデータを取得
res = req.urlopen(url)

# BeautifulSoupで解析
soup = BeautifulSoup(res, "html.parser")

yokais = soup.select(".yokai")
for yokai in yokais:
    print(yokai.string)
