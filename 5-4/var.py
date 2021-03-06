import tensorflow as tf

# 定数を定義
a = tf.constant(120, name="a")
b = tf.constant(130, name="b")
c = tf.constant(140, name="c")

# 変数を定義
v = tf.Variable(0, name="v")

# データグラフを定義
calc_op = a + b + c
assign_op = tf.assign(v, calc_op)

# セッションにて実行する
sess = tf.Session()
sess.run(assign_op)

# vの内容を表示する
print(sess.run(v))
