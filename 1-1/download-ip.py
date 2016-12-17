#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request

# データを取得する
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

# バイナリ文字列に変換
text = data.decode("utf-8")
print(text)
