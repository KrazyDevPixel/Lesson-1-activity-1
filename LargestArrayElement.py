def MEA(a):
    leng=len(a)
    if leng==1:
        return a[0]
    return max(a[0],MEA(a[1:]))
arr=[1342,4234,423,43274,4353442341029178219755]
print("biggest:",MEA(arr))