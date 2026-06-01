import math
import random
def value_pi():
    n=int(input("Enter the number of points you want to enter:"))
    inside_circle=0
    for i in range(1,n+1):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        distance=x*x+y*y
        if distance<=1:
            inside_circle+=1
    pi_estamited=(4*inside_circle)/n
    print(f"Estimated pi:{pi_estamited:.6f}")
    print(f"Actual_pi:{math.pi:.6f}")
    
value_pi()