#tower of hanoi program to move n disks
def hanoi(n,a,b,c):
    if n==1:
        print("move disk 1 from the rod",a,"to rod",c)
        return
    hanoi(n-1,a,b,c)
    print("move disk",n,"from rod",a,"to rod",b)
    hanoi(n-1,c,b,a)
n=3
hanoi(n,'A','B','C')
    