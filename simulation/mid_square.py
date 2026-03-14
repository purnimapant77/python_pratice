# Random Number Generation using Mid Square Method

seed = int(input("Enter seed value (4 digit number): "))
n = len(str(seed))
X = seed

print("\nStep  Xi        Xi^2        Middle Digits   Ri")


for i in range(1, 11):
    squared = X * X
    squared_str = str(squared).zfill(2 * n)
    start = (len(squared_str) - n) // 2
    middle = squared_str[start : start + n]
    X = int(middle)
    Ri = X / (10 ** n)
    print(f"X{i:<5} {X:<10} {squared:<12} {middle:<16} {Ri:.4f}")