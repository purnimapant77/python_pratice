import random

def coin_toss():
    print("COIN TOSS GAME")
    n = int(input("Enter number of tosses: "))

    heads = 0
    tails = 0

    for i in range(1, n + 1):
        result = random.randint(0, 1)
        if result == 0:
            heads += 1
        else:
            tails += 1

    print(f"\nTotal Tosses: {n}")
    print(f"Heads (H): {heads}")
    print(f"Tails (T): {tails}")
    print(f"\nProbability of Heads = {heads}/{n} = {heads/n:.4f}")
    print(f"Probability of Tails = {tails}/{n} = {tails/n:.4f}")
    print(f"\nTheoretical Probability = 0.5000")

    if abs(heads/n - 0.5) < 0.05:
        print("\nResult: Coin is FAIR (close to 50-50)")
    else:
        print("\nResult: Coin is BIASED (not close to 50-50)")

coin_toss()