def GML(a,a_size):
    C=0
    MO=0
    for i in range(0,a_size):
        if (a[i]==0):
            C=0
        else:
            C+=1
            MO=max(MO,C)
    return MO
a=[1,1,0,1,1,1]
a_size=len(a)
print(GML(a,a_size))
