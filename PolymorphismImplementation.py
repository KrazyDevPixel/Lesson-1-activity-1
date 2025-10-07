# Polymorphism Implementation
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a cat, my name is {self.name} and I'm {self.age} years old.")  
    def sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a dog, my name is {self.name} and I'm {self.age} years old.")
    def sound(self):
        print("Woof")

cat1 = Cat("Pudding", 6)
dog1 = Dog("Kiki", 3)

for animal in (cat1, dog1):
    animal.sound()
    animal.info()
