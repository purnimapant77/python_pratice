l=[]
for i in range(10):
    l.append(i**2) 
print(l)

li=[]
'''for i in range(5):
    li.append(input("Enter a number: "))
print(li)'''

cubes=[i**3 for i in range(5)]
print(cubes)

numbers=[1,2,3,4,5,2,3,4,7,8,9,10,2]
print(list(set(numbers)))


#append, extend and insert
my_list=[4,5,6,7]
my_list.append(6)
print(my_list)
my_list.extend([1,2,3])
print(my_list)
my_list.insert(2,10)
print(my_list)