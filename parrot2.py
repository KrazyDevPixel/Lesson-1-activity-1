class Parrot:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def song(self,song):
        return("{} sings {}".format(self.name,song))
    def dance(self):
        return("{} started dancing".format(self.name))
Blu=Parrot("Blue",14)
print(Blu.song("'Happy'"))
print(Blu.dance())
