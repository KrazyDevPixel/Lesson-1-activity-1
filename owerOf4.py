def po4(number):
    count=0
    if(number & (~(number & (number-1)))):
        while(number>1):
            number>>=1
            count+=1
        if(count%2==0):
            return True
        else:
            return False
num=int(input("Enter a number:"))
if(po4(num)):
    print("\nThe number is power of 4")
else:
    print("\nThe number is not power of 4")