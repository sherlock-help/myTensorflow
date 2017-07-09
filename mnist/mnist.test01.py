from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import argparse
import sys

FLAGS = None

def main(_):
    mnist = input_data.read_data_sets(FLAGS.data_dir,one_hot=True)

    x = tf.placeholder(tf.float32,[None, 784])
    W = tf.Variable(tf.zeros([784,10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.matmul(x,W) + b #matmul means matrix multiplication

    #defince the loss and optimizer
    y_ = tf.placeholder(tf.float32,[None,10])

    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y,y_))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)#o.5  is learning rate

    sess = tf.InteractiveSession()

    #train
    tf.global_variables_initializer().run()

    for _ in range(1000): # we will run the train step 1000 times
        batch_xs, batch_ys = mnist.train.next_batch(100) # batch size, for each iteration, we only use 100 points of the dataset
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})


    #test
    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default='dataset', help="Directory for storing data")
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main = main, argv=[sys.argv[0]] + unparsed)
