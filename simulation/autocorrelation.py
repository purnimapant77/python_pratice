# Autocorrelation Test for Independence

import math

def autocorrelation_test():
    n = int(input("Enter number of random numbers: "))
    numbers = []

    for i in range(n):
        x = float(input(f"R{i+1}: "))
        numbers.append(x)

    max_lag = int(input("Enter maximum lag: "))

    mean = sum(numbers) / n
    print("Mean =", round(mean,4))

    denom = sum((xi - mean) ** 2 for xi in numbers)

    print("\nLag   Autocorrelation")

    results = []
    for h in range(1, max_lag + 1):

        numer = sum((numbers[i] - mean) * (numbers[i + h] - mean) for i in range(n - h))

        if denom == 0:
            r = 0
        else:
            r = numer / denom

        results.append((h, r))

        if abs(r) < 0.3:
            verdict = "Independent"
        else:
            verdict = "Dependent"

        print(h, "   ", round(r,4), "  ", verdict)

    print("\nConclusion:")

    all_independent = all(abs(r) < 0.3 for _, r in results)

    if all_independent:
        print("Accept H0: Numbers are independent")
    else:
        print("Reject H0: Numbers are not independent")

    se = 1 / math.sqrt(n)
    z = 1.96

    upper = z * se
    lower = -z * se

    print("95% Confidence Interval:", round(lower,4), "to", round(upper,4))


autocorrelation_test()