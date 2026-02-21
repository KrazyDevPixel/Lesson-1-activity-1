def sas(arr,n,sum):
    for i in range(n):
        cs=arr[i]
        j=i+1
        while j<=n:
            if cs==sum:
                print("Sum found between")
                print("indexes % d and % d"%(i,j-1))
                return 1
            if cs>sum or j==n:
                break
            cs=cs+arr[j]
            j+=1
    print("No subarray found")
arr=[1,2,3,7,5]
n=len(arr)
sum=12
sas(arr,n,sum)