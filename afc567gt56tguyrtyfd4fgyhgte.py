def fun3(n):
    product = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            product *= j
    return product

print(fun3(4))
