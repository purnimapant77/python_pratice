# Generate 10 random numbers using Linear Congruential Method (LCM)

def linear_congruential():
    print("LINEAR CONGRUENTIAL METHOD")
    print("Formula: X(n+1) = (a * Xn + c) mod m\n")

    # Input parameters
    X = int(input("Enter Seed X0: "))
    a = int(input("Enter Multiplier a: "))
    c = int(input("Enter Increment c: "))
    m = int(input("Enter Modulus m: "))

    numbers = []

    for i in range(1, 11):
        X = (a * X + c) % m       # LCM formula
        Ri = X / m                # Normalize
        numbers.append(Ri)
        print(f"R{i} = {Ri:.4f}")

    # Statistics
    print(f"Min  = {min(numbers):.4f}")
    print(f"Max  = {max(numbers):.4f}")
    print(f"Mean = {sum(numbers)/len(numbers):.4f} (Ideal = 0.5)")

linear_congruential()