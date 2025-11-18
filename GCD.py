numlrg=int(input("Enter the largest number: "))
numsmll=int(input("Enter the smallest number: "))
while(numsmll):
    numstore=numsmll
    numsmll=numlrg%numsmll
    numlrg=numstore
print("HCF is: ",numlrg)