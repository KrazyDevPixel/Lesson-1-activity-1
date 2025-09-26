class student:
    grade=3
    name="Arham"
    def introduction(self):
        print('Hello everyone!')
    def details(self):
        print('My name is ',self.name)
        print('I read in grade ',self.grade)
ob=student()
ob.introduction()
ob.details()    