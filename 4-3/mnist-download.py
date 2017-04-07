#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request as req
import gzip, os, os.path

savepath = r"./mnist"
baseurl = r"http://yann.lecun.com/exdb/mnist"
files = [
    "train-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz"]

# ディレクトリ確認（なければ作成)
if not os.path.exists(savepath):
    os.mkdir(savepath)

# ダウンロード
for f in files:
    url = baseurl + "/" + f
    loc = savepath + "/" + f
    print("download : ", url)
    if not os.path.exists(loc):
        req.urlretrieve(url, loc)

# GZip回答
for f in files:
    gz_file = savepath + "/" + f
    raw_file = savepath + "/" + f.replace(".gz", "")
    print("gzip:", f)
    with gzip.open(gz_file, "rb") as fp:
        body = fp.read()
        with open(raw_file, "wb") as w:
            w.write(body)
print("ok")
