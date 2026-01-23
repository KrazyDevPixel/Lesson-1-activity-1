def p2l(a,a_size):
    l=sl=-2147483648
    for i in range(a_size):
        if (a[i]>l):
            sl=l
            l=a[i]
        elif(a[i]>sl and a[i]!=l):
            sl=a[i]
    print(sl)
arr=[1,4,5,2,5,3,6,8,3,6]
a_size=len(arr)
p2l(arr,a_size)        
