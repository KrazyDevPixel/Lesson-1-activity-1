import numpy as np
dt=[('name','S10'),('class',int),('height',float)]
sd=[('James',5,48.5),('Rohit',6,50.5),('Suresh',7,52.5),('Sanjay',8,54.5)]
st=np.array(sd,dtype=dt)
print("Original array: ")
print(st)
print("\nSort by height: ")
print(np.sort(st,order='height'))