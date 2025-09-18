#operations on dictionary
my_dict={}
my_dict={1:"Apple",2:"Ball"}
my_dict={'name':'john','age':17,1:[2,4,3]}
my_dict={'Name':'Jack','age':26}
#output : jack
print(my_dict['Name'])
print(my_dict.get('age'))
my_dict['age']=27
print(my_dict)
#qadd item
my_dict["city"]="Delhi"
print(my_dict)
my_dict.pop("age")
print(my_dict)
print("City:",my_dict.get("city"))
my_dict.clear()
print(my_dict)