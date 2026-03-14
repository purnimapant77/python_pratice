import math

def ks_test():
    # Input
    n = int(input("Enter number of random numbers: "))
    numbers = []
    print(f"Enter {n} random numbers (between 0 and 1):")
    for i in range(n):
        x = float(input(f"R{i+1} = "))
        numbers.append(x)

    # Sort numbers
    numbers.sort()

    D_plus_max = 0
    D_minus_max = 0

    for i in range(1, n + 1):
        Ri = numbers[i - 1]
        D_plus  = abs(i/n - Ri)
        D_minus = abs(Ri - (i-1)/n)

        if D_plus > D_plus_max:
            D_plus_max = D_plus
        if D_minus > D_minus_max:
            D_minus_max = D_minus

    D_max = max(D_plus_max, D_minus_max)
    critical_value = 1.36 / math.sqrt(n)

    # Output
    print(f"\nD+ max = {D_plus_max:.4f}")
    print(f"D- max = {D_minus_max:.4f}")
    print(f"D max  = {D_max:.4f}")
    print(f"Critical Value = {critical_value:.4f}")

    if D_max < critical_value:
        print("Numbers are uniformly distributed (ACCEPT H0)")
    else:
        print("Numbers are NOT uniformly distributed (REJECT H0)")

ks_test()