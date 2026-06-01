import math
import random
def area():
    a=float(input("enter lower limit a:"))
    b=float(input("enter upper limit b:"))
    n=int(input("Enter the number of random points:"))
    def func(x):
        return x**2
    actual=(b**3-a**3)/3
    total=0
    for i in range(n):
        x=random.uniform(a,b)
        total+=func(x)
    estimated=(b-a)*total/n