import numpy as np

def relu(x):
    return np.maximum(0, x)

class SingleLayer:
    def __init__(self, W, b):
        self.W = W
        self.b = b

    def forward(self, x):
        return relu(np.dot(x, self.W) + self.b)

class MLP_3Layer:
    def __init__(self, W1, W2, W3, b1, b2, b3):
        self.W1 = W1
        self.W2 = W2
        self.W3 = W3
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3

    def forward(self, x):
        l1 = SingleLayer(self.W1, self.b1)
        z1 = l1.forward(x)
        l2 = SingleLayer(self.W2, self.b2)
        z2 = l2.forward(z1)
        l3 = SingleLayer(self.W3, self.b3)
        z3 = l3.forward(z2)
        return z3


x = np.array([[1.0, 0.5], [-0.3, -0.2], [0.0, 0.8], [0.3, -0.4]])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([0.1, 0.2, 0.3])
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
b3 = np.array([0.1, 0.2])
layer = MLP_3Layer(W1, W2, W3, b1, b2, b3)
print(layer.forward(x))