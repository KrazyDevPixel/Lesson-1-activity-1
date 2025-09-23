#operations on sets
set={1,2,2,4,4}
print(set)
set.add(6)
print(set)

set1=set
set2={4,5,6,6}
print("\n set 1",set1)
print("set 2",set2)
print("Difference")
print(set1.difference(set2))
print("Symmetric difference")
print(set1.symmetric_difference(set2))
