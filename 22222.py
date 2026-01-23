def mie(a,size):
    temp=a[0]
    for i in range(1,size):
        temp=min(temp,a[i])
    return temp
def mae(a,size):
    temp=a[0]
    for i in range(1,size):
        temp=max(temp,a[i])
    return temp
arr=[1,4,5,2,5,3,6,8,3,6]
size=len(arr)
print("Minimum is:",mie(arr,size))
print("Maximum is:",mae(arr,size))