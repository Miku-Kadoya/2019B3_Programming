import numpy as np

class Affine():
    def __init__(self):
        self.x = None
        self.W = None
        self.b = None
        self.z = None
        self.dW = None
        self.db = None
        self.dx = None
    def forward(self, x, W, b):
        self.x = x
        self.W = W
        self.b = b
        self.z = np.dot(x, W) + b
        return self.z
    def backprop(self, dz):
        self.dW = np.dot(self.x.T, dz)
        self.db = np.sum(dz, axis=0)
        self.dx = np.dot(dz, self.W.T)
        return self.dW, self.db, self.dx


def main():
    x = np.array([[1.0, 0.5], [-0.4, 0.1]])
    W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    b = np.array([0.1, 0.2, 0.3])
    aff = Affine()
    print("順伝播出力: \n", aff.forward(x, W, b))
    dW, db, dx = aff.backprop(np.ones_like(W))
    print("逆伝播出力dx: \n", dx)
    print("逆伝播出力dW: \n", dW)
    print("逆伝播出力db: \n", db)

if __name__=="__main__":
    main()