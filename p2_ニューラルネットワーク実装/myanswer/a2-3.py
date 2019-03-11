import numpy as np

def relu(x):
    return np.maximum(0, x)

class SingleLayer:
    def __init__(self, x, W, b):
        self.x = x
        self.W = W
        self.b = b

    def forward(self):
        return relu(np.dot(self.W.T, self.x) + self.b)

x = np.array([1.0, 0.5])
W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b = np.array([0.1, 0.2, 0.3])
l = SingleLayer(x, W, b)
print(l.forward())