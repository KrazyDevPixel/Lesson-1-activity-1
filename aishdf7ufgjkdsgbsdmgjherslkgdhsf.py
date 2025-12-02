def reverseBits(n):
    ans = 0
    while n > 0:
        ans <<= 1
        if (n & 1) == 1:
            ans |= 1
        n >>= 1
    return ans
if __name__ == "__main__":
    n = 11
    print(reverseBits(n))