#Double check number python with nested if statements
num=int(input("Enter a number: "))
if num>50:
    print("the number is greater than 50")
    if num%2==0:
        print("And the number is even")
    else:
        print("And the number is odd")
else:
    print("the number is less than or equal to 50")