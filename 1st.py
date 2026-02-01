def rev(a,size,n):
    temp=0
    while(temp<size):
        s=temp
        end=min(temp+n-1,size-1)
        while(s<end):
            a[s],a[end]=a[end],a[s]
            s+=1
            end-=1
        temp+=n
a=[5,23,34,2,89,1,4,90]
n=2
size=len(a)
rev(a,size,n)
for i in range(0,size):
    print(a[i],end=" ")
