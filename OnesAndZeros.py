def numofbits(n):
    ones=0
    zeros=0
    while(n):
        if(n&1==1):
            ones+=1
        else:
            zeros+=1
        n>>=1
    print("\n\n Ones: ",ones,"\nZeros: ",zeros)
num=int(input("Enter a number: "))
numofbits(num)
