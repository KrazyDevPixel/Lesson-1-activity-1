def ebp(arr):
    lss=0
    rss=0
    n=len(arr)
    for i in range(n):
        lss=0
        rss=0
        for j in range(i):
            lss+=arr[j]
            for j in range(i+1,n):
                rss+=arr[j]
            if lss==rss:
                return i
    return -1
arr=[-7,1,5,2,-4,3,0]
print([ebp(arr)])            