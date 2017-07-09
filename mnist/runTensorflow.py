#导入tensorflow
import tensorflow as tf
#运行TensorFlow的InteractiveSession
sess = tf.InteractiveSession()

#我们通过为输入图像和目标输出类别创建节点，来开始构建计算图。
x = tf.placeholder("float", shape=[None, 784])
y_ = tf.placeholder("float", shape=[None, 10])

#变量 变量代表着TensorFlow计算图中的一个值
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

sess.run(tf.initialize_all_variables())
