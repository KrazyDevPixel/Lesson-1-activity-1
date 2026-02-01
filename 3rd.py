def led(a,asd):
    cm=a[asd-1]
    print(cm)
    for i in range(asd-2,-1,-1):
        if cm<a[i]:
            print(a[i])
            cm=a[i]
a=[5,23,34,2,89,1,4,90]
led(a,len(a))