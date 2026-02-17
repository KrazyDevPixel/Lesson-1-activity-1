def msas(a,a_size):
    max= -99999999999
    cmax=0
    for i in range(0,a_size):
        cmax=cmax+a[i]
        if(max<cmax):
            max=cmax
        if cmax<0:
            cmax=0
    return max
a=[-2,1,-3,4,-1,2,1,-5,4]
print(msas(a,len(a)))