import numpy as np

def softmax(x):
    max = np.max(x, axis=1, keepdims=True)
    x = x - max
    #print(x.size)
    exp_x = np.exp(x)
    sum = np.sum(exp_x, axis=1, keepdims=True)
    #print(sum.size)
    return exp_x / sum

class SoftmaxCrossEntropy():
    def __init__(self):
        self.x = None
        self.t = None
        self.y = None
        self.L = None
    def forward(self, x, t):
        self.x = x
        self.t = t
        self.y = softmax(x)
        L = np.sum(-t * np.log(self.y), axis=1)
        self.L = np.average(L, axis=0)
        return self.L
    def backprop(self, dL):
        return dL * (self.y - self.t)

x = np.array([[1.0, 0.5], [-0.4, 0.1]])
t = np.array([[1.0, 0.0], [0.0, 1.0]])
sce = SoftmaxCrossEntropy()
print("順伝播出力: \n", sce.forward(x, t))
print("逆伝播出力: \n", sce.backprop(1))
