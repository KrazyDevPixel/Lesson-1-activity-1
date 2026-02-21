def minimal(arr):
    ct0=0
    ct1=0
    for element in arr:
        if element==1:
            ct0+=1
        else:
            ct1+=1
    return min(ct0,ct1)
array1=[0,0,1,1,0,1,1]
print(f"array {array1}")
print(f"Minimum number of flips required: {minimal(array1)}")
array2=[0,0,0,0]
print(f"array {array2}")
print(f"Minimum number of flips required: {minimal(array2)}")
array3=[1,1,1,1]
print(f"array {array3}")
print(f"Minimum number of flips required: {minimal(array3)}")