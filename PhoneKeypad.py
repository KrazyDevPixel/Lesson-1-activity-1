kp=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
def prcomb(combination,curr,output,n):
    if(curr==n):
        print(*output,sep=",")
        return
    for i in range(len(kp[combination[curr]])):
        output.append(kp[combination[curr]][i])
        prcomb(combination,curr+1,output,n)
        output.pop()
        if(combination[curr]==0 or combination[curr]==1):
            break
combination=[2,3,4]
n=len(combination)
prcomb(combination,0,[],n)