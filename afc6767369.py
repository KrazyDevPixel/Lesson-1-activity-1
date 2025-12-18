def fss(s):
    res=[]
    for i in range(len(s)):
        for j in range(i,len(s)):
            res.append(s[i:j+1])
    return res
s=input("Enter a string: ")
res=fss(s)
for i in res:
    print(i, end='')
