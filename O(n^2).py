def ONsqauretime(n):
    iterations=0
    for i in range(0,n):
        for j in range(0,n):
            print("* ",end="")
            iterations+=1
        print("")
    print("\n When n is ",n," total iterations done by code: ",iterations,"\n")
ONsqauretime(5)
ONsqauretime(4)
ONsqauretime(3)
print("\n With every 'n' the time taken equals n^2")
print("0(n^2)")