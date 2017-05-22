import pandas as pd
from sklearn import svm, metrics, cross_validation
import random, re

# アヤメのCSVデータを読み込む
csv = pd.read_csv('data/iris.csv')

# リストを訓練データとラベルに分割する
data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
label = csv["Name"]

# クロスバリデーションを使う
clf = svm.SVC()
scores = cross_validation.cross_val_score(clf, data, label, cv=5)
print("各種正解率 = ", scores)
print("正解率 = ", scores.mean())
