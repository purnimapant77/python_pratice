def chi_square_test():
    # Input
    n = int(input("Enter total number of random numbers: "))
    k = int(input("Enter number of class intervals: "))
    numbers = []

    for i in range(n):
        numbers.append(float(input(f"R{i+1} = ")))

    # Count observed frequency in each interval
    observed = [0] * k
    for x in numbers:
        idx = int(x * k)
        if idx == k:  # in case x=1
            idx = k - 1
        observed[idx] += 1

    expected = n / k
    chi_square = 0

    for i in range(k):
        chi_square += ((observed[i] - expected) ** 2) / expected

    df = k - 1
    chi_sq_table = {
        1: 3.841, 2: 5.991, 3: 7.815, 4: 9.488,
        5: 11.070, 6: 12.592, 7: 14.067, 8: 15.507,
        9: 16.919, 10: 18.307
    }

    print(f"\nChi-Square Calculated = {chi_square:.4f}")
    print(f"Degrees of Freedom    = {df}")

    if df in chi_sq_table:
        critical = chi_sq_table[df]
        print(f"Chi-Square Critical   = {critical:.3f}")
        if chi_square < critical:
            print("ACCEPT H0")
        else:
            print("REJECT H0")
    else:
        print(f"Please check Chi-Square table for df={df}")

chi_square_test()