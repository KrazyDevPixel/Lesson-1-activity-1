def one_to_ten(n):
    if (n<10):
        return
    print(n)
    one_to_ten(n+1)
one_to_ten(1)
