# Dice Toss Game Simulation

import random

def dice_toss_game():

    games = int(input("Enter number of games to simulate: "))

    wins = 0
    losses = 0

    for game in range(1, games + 1):

        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        total = d1 + d2

        print("\nGame", game)
        print("First Roll:", d1, "+", d2, "=", total)

        if total in [7,11]:
            print("Result: WIN (7 or 11)")
            wins += 1

        elif total in [2,3,12]:
            print("Result: LOSE (2,3,12)")
            losses += 1

        else:
            point = total
            print("Point =", point)

            rolls = 0
            while True:
                rolls += 1
                d1 = random.randint(1,6)
                d2 = random.randint(1,6)
                new_total = d1 + d2

                print("Roll", rolls, ":", d1, "+", d2, "=", new_total)

                if new_total == point:
                    print("Result: WIN")
                    wins += 1
                    break

                elif new_total == 7:
                    print("Result: LOSE")
                    losses += 1
                    break

    print("\nTotal Games:", games)
    print("Wins:", wins)
    print("Losses:", losses)

    print("Win % =", round((wins/games)*100,2))
    print("Loss % =", round((losses/games)*100,2))


dice_toss_game()