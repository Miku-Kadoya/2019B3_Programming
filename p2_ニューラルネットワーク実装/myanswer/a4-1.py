import numpy as np
from test.a3-2 import ReLU
from test.a3-4 import Affine
from test.a3-5 import SoftmaxCrossEntropy

class NeuralNetwork():
    def __init__(self):
        self.param_names = ["W1", "b1", "W2", "b2"]
        self.params = {}
        self.params_grad = {}
        self.params["W1"] = np.random.normal(0., 0.1, [784, 500])
        self.params["b1"] = np.zeros([500])
        self.params["W2"] = np.random.normal(0, 0.1, [500, 10])
        self.params["b2"] = np.zeros([10])

        self.affine1 = Affine()
        self.affine2 = Affine()
        self.relu = ReLU()
        self.softcrossent = SoftmaxCrossEntropy()

    def forward(self, x):
        z1 = self.affine1.forward(x, self.params['W1'], self.params['b1'])
        z2 = self.relu.forward(z1)
        z3 = self.affine2.forward(z2, self.params['W2'], self.params['b2'])
        return z3

    def loss(self, x, t):
        return self.softcrossent.forward(self.forward(x), t)

    def backprop(self, x, t):
        self.loss(x, t)
        dz3 = self.softcrossent.backprop(1)
        dz2, self.params_grad['W2'], self.params_grad['b2'] = self.affine2.backprop(dz3)
        dz1, self.params_grad['W1'], self.params_grad['b1'] = self.affine1.backprop(dz2)

    def sgd(self, x, t, learning_rate):
        self.backprop(x, t)
        for param in self.param_names:
            self.params[param] -= learning_rate * self.params_grad[param]
