class Person():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print("First name:",self.fname)
        print("Last name:",self.lname)
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year
x=Student("Soheni","Das",2016)
x.display()
print("Graduation Year:",x.graduationyear)