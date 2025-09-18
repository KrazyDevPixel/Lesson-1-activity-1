#list to dictionary
def test(lst):
    result={}
    for item in lst:
        result[item[0]]=item[1:]
    return result
students=[['John',21,'A'],['Jane',22,'B'],['Jim',23,'C']]
print("Original list:",students)
print("Converted list to dictionary")
print(test(students))
