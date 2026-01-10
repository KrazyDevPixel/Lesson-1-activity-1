def cs(a):
    len_a = len(a)
    if len_a == 1 or len_a == 0:
        return True
    return a[0] <= a[1] and cs(a[1:])
a=[1,2,3,4,5,6,7,8]
if cs(a):
    print("Sorted")
else:
    print("Not Sorted")