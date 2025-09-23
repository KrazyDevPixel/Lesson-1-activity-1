#ops on tuples
my_tuple=()
print(my_tuple)
my_tuple=(1,2,3,4,5)
print(my_tuple)
my_tuple=('hi',7,8.8)
print(my_tuple)
my_tuple=('Word',[8,3,6],(1,2,3))
print(my_tuple)
#accessing elements
my_tuple=('H','e','l','l','o')
print(my_tuple[0])
print(my_tuple[4])
#nested tuple
n_tuple=('Hie',[8,3,6],(1,2,3))
#nested index
print(n_tuple[0][2])
print(n_tuple[1][1])
#sliced
print(my_tuple[1:4])
#iterating through a tuple
for letter in (my_tuple):
    print('Hello',letter)