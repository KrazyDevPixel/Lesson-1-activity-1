def id(n,num):
    if (n<1 or n>num):
        return
    print(n)
    id(n-1,num)
    print(n)
x=int(input("Enter number you want to print start:"))
id(x,x)