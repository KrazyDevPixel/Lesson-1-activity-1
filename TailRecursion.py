def tr(n,num):
    if n>num:
        return
    print(n)
    tr(n+1,num)
x=int(input("Enter number you want to print start:"))
tr(1,x)