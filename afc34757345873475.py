import cmath

class Exp:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def solve(self):
        result = (7 * self.x) / (3 * self.y)
        print("result:", result)

# Instantiate and solve
ob = Exp(2, 2)
ob.solve()
