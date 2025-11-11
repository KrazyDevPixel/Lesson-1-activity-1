num=int(input("Enter a number: "))
digits=len(str(num))
resultnum=0
tempnum=num
while tempnum>0:
    digit=tempnum%10
    resultnum+=digit**digits
    tempnum//=10
if num==resultnum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")