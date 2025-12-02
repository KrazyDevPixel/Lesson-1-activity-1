def pr2od(arr, size):
    xor2 = arr[0]
    x = 0
    y = 0
    
    # XOR all numbers
    for i in range(1, size):
        xor2 = xor2 ^ arr[i]

    # Get rightmost set bit of xor2
    setbit = xor2 & -xor2   # simpler and safer than ~(xor2 - 1)

    # Divide numbers into two sets based on setbit
    for num in arr:
        if num & setbit:
            x = x ^ num
        else:
            y = y ^ num

    print("The two odd occurring elements are:", x, "and", y)


# Input handling
arr_size = int(input("Enter array size: "))
arr = []

for i in range(arr_size):
    z = int(input("Enter element: "))
    arr.append(z)

pr2od(arr, arr_size)
