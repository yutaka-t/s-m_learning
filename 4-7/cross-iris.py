#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sklearn import svm, metrics
import random, re
import os

# アヤメのCSVデータを読み取る
lines = open("./data/iris.csv", 'r', encoding='utf-8').read().split("\n")
f_tonum = lambda n: float(n) if re.match(r'^[0-9]+$', n) else n
f_cols = lambda li: list(map(f_tonum, li.strip().split(',')))
csv = list(map(f_cols, lines))
# 先頭のヘッダー行を削除
del csv[0]
# データをシャッフル
random.shuffle(csv)

# データをK分割する
k = 5
# リストの中に、空のリストをk個作成
csvk = [[] for i in range(k)]
print(csvk)
for i in range(len(csv)):
    csvk[i % k].append(csv[i])

print(csvk)


# リストを訓練データとラベルに分ける関数
def split_data_label(rows):
    data = []
    label = []
    for row in rows:
        data.append(row[0:4])
        label.append(row[4])
    # return (data, label)
    return data, label


# 正解率を求める
def calc_score(test, train):
    test_f, test_l = split_data_label(test)
    train_f, train_l = split_data_label(train)
    # 訓練データを学習して正解率を求める
    clf = svm.SVC()
    clf.fit(train_f, train_l)
    pre = clf.predict(test_f)
    return metrics.accuracy_score(test_l, pre)


# k分割したデータについて正解率を求める
score_list = []
for testc in csvk:
    # testc意外のデータを訓練データとする
    trainc = []
    for i in csvk:
        if i != testc:
            trainc += i
    sc = calc_score(testc, trainc)
    # print("sc : ", sc)
    score_list.append(sc)
print("各正解率=", score_list)
print("平均正解率=", sum(score_list) / len(score_list))
