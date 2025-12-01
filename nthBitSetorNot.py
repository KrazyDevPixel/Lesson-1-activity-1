def setornot(number,n):
   if number & (1<<(n-1)):
        print("\n SET")
   else:
        print("\n NOT SET")
num=int(input("Enter a number: "))
n=int(input("Enter the bit NUMBER: "))
setornot(num,n)