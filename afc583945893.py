def SORT(a,a_size):
    zero=0
    one=0
    two=a_size-1
    while one<=two:
        if a[one]==0:
            a[zero],a[one]=a[one],a[zero]
            zero+=1
            one+=1
        elif a[one]==1:
            one+=1
        else:
            a[one],a[two]=a[two],a[one]
            two-=1
a=[5,3,6,7,4,7,8,6,8,6,5,1,0,2,1,0,2,1,0]
a_size=len(a)
print(a)
SORT(a,a_size)
print(a)
