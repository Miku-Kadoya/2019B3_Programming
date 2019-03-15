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