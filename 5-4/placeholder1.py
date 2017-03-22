import tensorflow as tf

# プレースホルダを定義
# 整数型の要素3個の配列
a = tf.placeholder(tf.int32, [3])

# 配列を2倍にする演算子を定義
b = tf.constant(2)
x2_op = a * b

# セッションを開始
sess = tf.Session()

# プレースホルダに値を当てはめて実行
r1 = sess.run(x2_op, feed_dict={a: [1, 2, 3]})
print(r1)
r2 = sess.run(x2_op, feed_dict={a: [10, 20, 10]})
print(r2)
