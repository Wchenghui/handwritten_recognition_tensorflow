import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
mnist=input_data.read_data_sets("MNIST_data/",one_hot=True)
sess = tf.InteractiveSession()
x_input=tf.placeholder(tf.float32,[None,784])
y_input=tf.placeholder(tf.float32,[None,10])
W1=tf.Variable(tf.random_normal([784,64],stddev=0.1))
b1=tf.Variable(tf.zeros([64]))+0.1
hidden=tf.nn.relu(tf.matmul(x_input,W1)+b1)
W2=tf.Variable(tf.random_normal([64,10],stddev=0.1))
b2=tf.Variable(tf.zeros([10]))+0.1
output=tf.nn.softmax(tf.matmul(hidden,W2)+b2)
#keep_prob = tf.placeholder(tf.float32)
loss=-tf.reduce_sum(y_input*tf.log(output+1e-6))
optimizer=tf.train.AdamOptimizer(1e-2)
train_step=optimizer.minimize(loss)
corret_prediction=tf.equal(tf.argmax(output,1),tf.argmax(y_input,1))
accuracy=tf.reduce_mean(tf.cast(corret_prediction,"float"))
saver = tf.train.Saver()
sess.run(tf.global_variables_initializer())
for i in range(20000):
    #print sess.run(b)
    batch = mnist.train.next_batch(100)
    sess.run(train_step,feed_dict={x_input:batch[0],y_input:batch[1]})
    if i%100==0:
        train_accuracy = accuracy.eval(feed_dict={x_input:batch[0],y_input:batch[1]})        
        print "step:",i," loss:",sess.run(loss,feed_dict={x_input:batch[0],y_input:batch[1]})," train Accuracy:",sess.run(accuracy,feed_dict={x_input:batch[0],y_input:batch[1]})

print("test accuracy %g"%accuracy.eval(feed_dict={x_input:mnist.test.images,y_input:mnist.test.labels}))
