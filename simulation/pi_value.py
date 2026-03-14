import random
import math

def find_pi():
    print("   VALUE OF PI ")
    print(" - We throw random points inside a 1x1 square")
    print(" - Count how many fall inside a quarter circle")
    print(" - PI = 4 * (points inside circle / total points)")
    n = int(input("\nEnter number of random points: "))

    inside_circle = 0

    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = x * x + y * y
        if distance <= 1:
            inside_circle += 1

    # Estimate PI
    pi_estimated = 4 * inside_circle / n

    print(f"\nTotal Points Generated : {n}")
    print(f"Points Inside Circle : {inside_circle}")
    print(f"Points Outside Circle : {n - inside_circle}")
    print(f"\nEstimated PI = 4 * {inside_circle} / {n}")
    print(f"Estimated PI = {pi_estimated:.6f}")
    print(f"Actual PI= {math.pi:.6f}")
    print(f"Error= {abs(math.pi - pi_estimated):.6f}")
find_pi()