def getFStSet(n):
    if n==0:
        return 0
    res=1
    while(n&1)==0:
        n= n>>1
        res+=1
    return res
if __name__== "__main__":
    n = int(input("Enter a number: "))
    print(getFStSet(n))