import numpy as np

class Multiply():
    def __init__(self):
        self.x = None
        self.y = None
    def forward(self, x, y):
        self.x = x
        self.y = y
        z = x * y
        return z
    def backprop(self, dz):
        dx = dz * self.y
        dy = dz * self.x
        return dx, dy

class Add():
    def __init__(self):
        self.x = None
        self.y = None
    def forward(self, x, y):
        self.x = x
        self.y = y
        z = x + y
        return z
    def backprop(self, dz):
        dx = dz
        dy = dz
        return dx, dy

a = 2
b = 3
c = 4
add = Add()
mul = Multiply()
print("順伝播出力: ", mul.forward(add.forward(a, b), c))
dz, dc = mul.backprop(1)
da, db = add.backprop(dz)
print("逆伝播出力 da: ", da, ", db: ", db, ", dc: ", dc)