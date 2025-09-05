age=int(input("Enter your age: "))
if age<12:
    print("You cannot give exams")
elif age>15:
    print("You can give 5th exam")
elif age>18:
    print("You can give 10th exam")
else:
    print("You can give 12th exam")