def maxdif(arr):
    if not arr or len(arr)<2:
        return 0
    return max(arr)-min(arr)
arr=[2,7,1,9,5]
print(maxdif(arr))
