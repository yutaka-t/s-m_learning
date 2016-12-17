#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request

# URLと保存パスを指定
url = "https://s.yimg.jp/images/mh/pc/jp/rd/1.0.0/yafuoku.png"
save_name = "yafuoku.png"

# ダウンロード
mem = urllib.request.urlopen(url).read()

# ファイルへ保存
with open(save_name, mode="wb") as f:
    f.write(mem)
    print("保存しました")
