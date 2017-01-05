#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse

# API = "http://api.aoikujira.com/zip/xml/get.php"
API2 = "http://api.aoikujira.com/zip/zip.php"

# パラメータ
values = {
    'fmt': 'xml',
    # 'fmt': 'json',
    'zn': '1010051'
}

# パラメータをURLエンコードする
params = urllib.parse.urlencode(values)

# リクエスト用のURLを生成
url = API2 + "?" + params
print("url=", url)

# ダウンロード
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
