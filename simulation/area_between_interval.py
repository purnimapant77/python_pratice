import random

def area_under_curve():
    print("Function: f(x) = x^2")

    a = float(input("\nEnter lower limit (a): "))
    b = float(input("Enter upper limit (b): "))
    n = int(input("Enter number of random points: "))

    def func(x):
        return x**2

    actual = (b**3 - a**3) / 3

    total = 0
    for i in range(n):
        x = random.uniform(a, b)
        total += func(x)

    estimated_area = (b - a) * total / n

    print(f"\nRandom Points: {n}")
    print(f"Estimated Area = {estimated_area:.6f}")
    print(f"Actual Area = {actual:.6f}")
    print(f"Error = {abs(actual - estimated_area):.6f}")

area_under_curve()