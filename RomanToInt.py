def romantoint(romanInput):
    roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    resultint=0
    for i in range(0,len(romanInput)-1):
        if roman[romanInput[i]]<roman[romanInput[i+1]]:
            resultint-=roman[romanInput[i]]
        else:
            resultint+=roman[romanInput[i]]
    return resultint+roman[romanInput[-1]]
romaninput=input("Enter a Roman numeral: ")
print("integer equivalent: ",romantoint(romaninput))