def hr(n,num):
    if n>num:
        return
    hr(n+1,num)
    print(n)
x=int(input("Ent6er number you want to print start:"))
hr(1,x)