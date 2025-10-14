fn1=open("rand.txt",'r')
print(file.read())
fn1.close()
fn=open("rand.txt",'w')
fn.write("Hello im arham 2")
file.close()
for i in range(1,len(cont)+1):
    if(i%2!=0):
        fn1.write(cont[i-1])
    else:
        pass
fn1.close()
fn1=open('rand.txt','r')
cont1=fn1.read()
print(cont1)
fn.close()
fn1.close()