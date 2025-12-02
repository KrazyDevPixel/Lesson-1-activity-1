def odoc(arr):
    res=0
    for element in arr:
        res=res^element
    return res
arr=[]
n=int(input("Enter array size: "))
while(n):
    n=int(input("Enter number: "))
    arr.append(n)
    n-=1
print("The odd occurring element is:",odoc(arr))