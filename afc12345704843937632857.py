def fac(n):
    if n == 1 or n == 0:
        return 1
    return n * fac(n - 1)
def printit010(n):
    if n > 10:
        return
    print(n)
    printit010(n + 1)
if __name__ == "__main__":
    num = 5
    print(f"Factorial of {num} is {fac(num)}")
    print("Printing numbers from 1 to 10:")
    printit010(1)