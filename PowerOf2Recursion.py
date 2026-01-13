n=int(input("enter a number: "))
def powerof2(n):
    if(n<=0):
        return False
    if (n==1):
        return True
    if (n%2==0):
        return powerof2(n//2)
    return False
if (powerof2(n)):
    print(f"{n} is a power of 2")
else:
    print(f"{n} is not a power of 2")
