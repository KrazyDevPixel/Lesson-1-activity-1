def rn(num):
    if(num>0):
        last=num%10
        if (num//10>0):
            cn=rn((int)(num//10))
            return last*(10**(len(str(cn))))+cn
        return num
n=int(input("Enter a number: "))
print("Reversed Number is:",rn(n))