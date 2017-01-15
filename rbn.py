import tensorflow as tf
from util import getData

class rbm:
    def __init__(self, shape, para, data):
        # shape[0] means the number of visible units
        # shape[1] means the number of hidden units
        self.para = para
        self.sess = tf.Session()
        self.data = datai
        stddev = 1.0 / np.sqrt(shape[0])
        self.W = tf.Variable(tf.random_normal([shape[0], shape[1]], stddev = stddev), name = "W")
        self.bv = tf.Variable(tf.zeros(shape[0]), name = "a")
        self.bh = tf.Variable(tf.zeros(shape[1])), name = "b")
        init_op = tf.global_variables_initializer()
        self.sess.run(init_op)
        self.buildModel()
        print "rbm init completely"
        pass
    def buildModel(self):
        self.v = tf.placeholder("float", [None, shape[0]])
        self.h = self.sample(tf.sigmoid(self.v * self.W + self.bh))
        #gibbs_sample
        v_sample = self.sample(tf.sigmoid(self.h * tf.transpose(self.W) + self.bv))
        h_sample = self.sample(tf.sigmoid(self.v_sample * self.W + self.bh))
        self.lr = self.para["learning_rate"] / tf.to_float(self.para["batch_size"])
        W_adder = self.W.assign_add(self.lr  * (tf.transpose(v) * h - tf.transpose(v_sample) * h_sample))
        bv_adder = self.bv.assign_add(self.lr * tf.reduce_mean(v - v_sample, 0))
        bh_adder = self.bh.assign_add(self.lr * tf.reduce_mean(h - h_sample, 0))
        self.upt = [W_adder, bv_adder, bh_adder]
    def doTrain(self):
        for epoch in range(self.para["epoch"]):
            np.random.shuffle(self.data)
            for i in range(0, len(self.data), self.para["batch_size"]):
                X = self.data[i:i + self.para["batch_size"]]
                self.sess.run(self.upt, feed_dict = {self.v : X})
        pass
    def sample(self, probs):
        return tf.floor(probs + tf.random_uniform(tf.shape(probs), 0, 1))
    def getWb(self):
        return self.sess.run([self.W, self.bv, self.bh])

if __name__ == "__main__":
    data = getData(dataSet)
    myRBM = rbm([data.shape[0], 200], {"batch_size": 64, "learning_rate":0.001}, data)
    myRBM.doTrain()
    W, bv, bh = myRBM.getWb()
