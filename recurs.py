#FActoria number using recursion
def factorial(n):
    if n==1:
        return n
    else:
        return n * factorial(n-1)
num=int(input("Enter a number to fiund the factorial of it: "))
#check if the4 num is negative
if num<0:
    print("Factorial does not exist for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of ",num," is ",factorial(num))