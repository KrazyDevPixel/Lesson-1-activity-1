def ats(a):
    leng=len(a)
    if leng==1:
        return a[0]
    return a[0]-ats(a[1:])
arr=[5,10,15,20,25]
print("total:",ats(arr))