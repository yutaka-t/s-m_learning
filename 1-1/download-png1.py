#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request

# URLと保存パスを指定
url = "https://www.google.co.jp/images/branding/googlelogo/2x/googlelogo_light_color_272x92dp.png"
save_name = "google.png"

# ダウンロード
urllib.request.urlretrieve(url, save_name)
print("保存しました")
