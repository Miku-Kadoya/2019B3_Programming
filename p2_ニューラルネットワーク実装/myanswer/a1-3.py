class Perceptron:
    def __init__(self, w1, w2, theta):
        self.w1 = w1
        self.w2 = w2
        self.theta = theta

    def forward(self, x1, x2):
        y = self.w1 * x1 + self.w2 * x2
        if y >= self.theta:
            return 1
        else:
            return 0

def xor(x1, x2):
    andg = Perceptron(0.5, 0.5, 0.7)
    nandg = Perceptron(-0.5, -0.5, -0.7)
    org = Perceptron(0.5, 0.5, 0.5)
    return andg.forward(nandg.forward(x1, x2), org.forward(x1, x2))

x1_list = [1, 1, 0, 0]
x2_list = [1, 0, 1, 0]
for i,j in zip(x1_list, x2_list):
    print("XOR({0}, {1}) = {2}".format(i, j, xor(i, j)))