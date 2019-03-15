import numpy as np

class ReLU():
    def __init__(self):
        self.x = None
    def forward(self, x):
        self.x = x
        z = x * (np.where(x > 0, 1, 0))
        return z
    def backprop(self, dz):
        return dz * (np.where(self.x > 0, 1, 0))

def main():
    x = np.array([-0.5, 0.0, 1.0, 2.0])
    y = ReLU()
    print("順伝播出力: ", y.forward(x))
    print("逆伝播出力: ", y.backprop(1.))

if __name__ == "__main__":
    main()