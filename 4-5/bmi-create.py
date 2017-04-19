#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random


# BMIを計算して体型を返す
def calc_bmi(h, w):
    bmi = w / (h / 100) ** 2
    if bmi < 18.5:
        return "thin"
    if bmi < 25:
        return "normal"
    return "fat"


# 出力ファイルの準備
fp = open("bmi.csv", "w", encoding="utf-8")
fp.write("height,weight,label\n")

# ランダムなデータ生成
cnt = {"thin": 0, "normal": 0, "fat": 0}
for i in range(4000):
    h = random.randint(120, 200)
    w = random.randint(35, 80)
    label = calc_bmi(h, w)
    cnt[label] += 1
    fp.write("{},{},{}\n".format(h, w, label))
fp.close()
print("ok , ", cnt)
