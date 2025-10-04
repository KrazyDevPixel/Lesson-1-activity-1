class Shape:
    def __init__(self):
        pass
    def get_area(self):
        raise NotImplementedError("Subclasses must implement get_area()")
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side) 
        self.side = side
    def set_side(self, new_side):
        self.side = new_side
        self.width = new_side
        self.height = new_side
rect = Rectangle(5, 10)
print(f"Rectangle area: {rect.get_area()}") 
square = Square(7)
print(f"Square area: {square.get_area()}")  
square.set_side(9)

print(f"New square area: {square.get_area()}")
