#parent class
class Person():
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number
    def display(self):
        print("Name:",self.name)
        print("ID Number:",self.id_number)
#child class
class Employee(Person):
    def __init__ (self,name,id_number,salary,post):
        Person.__init__(self,name,id_number)
        self.salary=salary
        self.post=post
a=Employee("Soheni das",34728321,999999578475834758748937834573485734895999999999,"SENIOR CODING INSTRUCTOR")
a.display()
print("TOO GOOD SALARY:",a.salary)
print("POST:",a.post)