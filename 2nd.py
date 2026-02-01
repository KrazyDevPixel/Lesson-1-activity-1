def rota(a,n,a_s):
    for i in range(n):
        rota(a,a_s)
def rotat(a,a_s):
    temp=a[0]
    for i in range(a_s-1):
        a[i]=a[i+1]
    a[a_s-1]=temp
def prar(a,a_s):
    for i in range(a_s):
        print("% d"%a[i],end=" ")
    print("\n")
a=[5,23,34,2,89,1,4,90]
prar(a,len(a))
rotat(a,len(a))
prar(a,len(a))