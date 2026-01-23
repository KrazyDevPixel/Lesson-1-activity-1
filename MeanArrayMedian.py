def arraymean(arr,arr_size):
    ts=0
    for i in range(0,arr_size):
        ts+=arr[i]
    return float(ts/arr_size)
def arraymed(arr,arr_size):
    sorted(arr)
    if arr_size%2!=0:
        return float(arr[arr_size//2])
    return float((arr[(arr_size//2)-1]+arr[arr_size//2])/2) 
arr=[1,4,5,2,5,3,6,8,3,6] 
arr_size=len(arr)
print("Mean is:",arraymean(arr,arr_size))
print("Median is:",arraymed(arr,arr_size))