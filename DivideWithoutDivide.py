def divide(ourdividend, ourdivisor):
    if ourdivisor == 0:
        raise ZeroDivisionError("division by zero")
    sign = -1 if ((ourdividend < 0) ^ (ourdivisor < 0)) else 1
    ourdividend = abs(ourdividend)
    ourdivisor = abs(ourdivisor)
    quotient = 0
    temp = 0
    for i in range(31, -1, -1):
        if temp + (ourdivisor << i) <= ourdividend:
            temp += ourdivisor << i
            quotient |= 1 << i
    return sign * quotient
a = int(input("enter a for a/b: "))
b = int(input("enter b for a/b: "))
print("The result of a/b is:", divide(a, b))
