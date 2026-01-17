def ways(stairs):
    if stairs<0:
        return 0
    if stairs==0:
        return 1
    TS=0
    OS=0
    if (stairs>=2):
        TS=ways(stairs-2)
    OS=ways(stairs-1)
    return TS+OS
n=int(input("Enter number of stairs: "))
print("Number of ways to climb",n,"stairs is:",ways(n))