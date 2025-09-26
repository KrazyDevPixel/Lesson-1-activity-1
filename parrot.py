#parrot
class Parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
Blu=Parrot("Blu",10)
Woo=Parrot("Woo",15)
print("Blu is {} years old.".format(Blu.age))
print("Woo is {} years old.".format(Woo.age))
print("{} is a {}.".format(Blu.name, Blu.species))
print("{} is a {}.".format(Woo.name, Woo.species))