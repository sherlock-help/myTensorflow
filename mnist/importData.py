
#MNIST是一个入门级的计算机视觉数据集

#import data
#from tensorflow.examples.tutorials.mnist import input_data
#mnist = input_data.read_data_sets("./dataset-mnist", one_hot=True)
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("dataset-mnist/", one_hot=True)
