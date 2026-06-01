import random
def coin_toss():
    num=int(input("Enter the number of samples:"))
    head=0
    tail=0
    for i in range(1,num+1):
        toss=random.randint(0,1)
        if toss==0:
            head+=1
        else:
            tail+=1
    print(f"total toss: {num}")
    print(f"total number of heads:{head}")
    print(f"total number of tails:{tail}")
    print(f"probability of heads:{head/num}")
    print(f"probability of tails:{tail/num}")
    print(f"Theoritical probability is 0.5 for both heads and tails")
    if abs(head/num -0.5)<0.05:
        print("Coin toss is fair")
    else:
        print("coin toss is biased")
    
coin_toss()