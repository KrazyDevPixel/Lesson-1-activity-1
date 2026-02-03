def fw(a,a_s):
    lt=[0]*a_s
    rt=[0]*a_s
    water=0
    lt[0]=a[0]
    for i in range(1,a_s):
        lt[i]=max(lt[i-1],a[i])
    rt[a_s-1]=a[a_s-1]
    for i in range(a_s-2,-1,-1):
        rt[i]=max(rt[i+1],a[i])
    for i in range(0,a_s):
        water+=min(lt[i],rt[i])-a[i]
    return water
a=[0,1,0,2,1,0,1,3,1,2,1]
bars=len(a)
print(fw(a,bars))