"""
Amy and Bill are playing a dice game where they take turn rolling a standard,
6-sided die. Amy rolls first. The winner is whoever rolls a 6 first.

What is the probability Amy wins?
"""

import random


def amy_bill_game(N: int = 1_000_000) -> float:
    outcomes = {"Amy": 0, "Bill": 0}
    die = [i for i in range(1, 6 + 1)]

    # Play game N times
    for _ in range(N):

        # Game continues until winner
        no_winner = True
        while no_winner:

            if random.choice(die) == 6:
                outcomes["Amy"] += 1
                no_winner = False
            elif random.choice(die) == 6:
                outcomes["Bill"] += 1
                no_winner = False
            else:
                continue

    return outcomes["Amy"] / N


if __name__ == "__main__":
    print(f"Simulation result: {amy_bill_game():.4f}")
    print(f"Analytical result: {6/11:.4f}")
