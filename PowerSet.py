import math
def pps(set, setsize):
    pss=(int)(math.pow(2,setsize))
    out=0;
    inn=0;
    for out in range(0,pss):
        for inn in range(0,setsize):
            if((out & (1<<inn))>0):
                print(set[inn],end="")
        print(" ")
size=int(input("Enter size of array: "))
set=[]
for i in range(0,size):
    n=int(input("enter element: "))
    set.append(n)
pps(set, len(set))