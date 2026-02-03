def cp(ar,ar_s):
    profit=0
    for i in range(1,ar_s):
        if ar[i]>ar[i-1]:
            profit+=ar[i]-ar[i-1]
    return profit
pri=[635,864,247,325,257,745,245]
prof=cp(pri,len(pri))
print(prof)