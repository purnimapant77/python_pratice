def add(a,b):
    print(a+b)
    
lambda_add= lambda a,b: a+b

add(2,3)
sum=lambda_add(2,3)
print(sum)


square=lambda x: x*2
print(square(4))

get_name=lambda: "Purnima"
print(get_name())

is_even=lambda x: "Even" if x%2==0 else "Odd"

print(is_even(5))
print(is_even(10))


my_list=[1,2,3,4,5]
squared_list=list(map(lambda x: x**2, my_list))
print(squared_list)