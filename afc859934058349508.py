# class square
class square:
    def __init__(self, side):
        self.side = side
    def area(self):
        print("My area is :", self.side * self.side)

# class circle
class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("My area is :", 3.14 * self.radius * self.radius)

# object creation
square1 = square(5)
circle1 = circle(5)

# iterating through objects
for shape in (square1, circle1):
    shape.area()
