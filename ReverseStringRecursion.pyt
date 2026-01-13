def rs(s):
    if len(s)==1:
        return s[0]
    fc=s[0]
    return rs(s[1:])+fc
s="allanannaallan"
print("Reversed String is:",rs(s))