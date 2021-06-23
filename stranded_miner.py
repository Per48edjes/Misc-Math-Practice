"""
From Interview Query: <https://www.interviewquery.com/questions/stranded-miner>

A miner is stranded and there are two paths he can take.

Path A loops back to itself and takes him 5 days to walk it.

Path B brings him to a junction immediately (0 days). The junction at the end of
Path B has 2 paths, say Path BA and Path BB.

Path BA brings him back to his original starting point and takes him 2 days to
walk. Path BB brings him to safety and takes him 1 day to walk.

Each path has an equal probability of being chosen and once a wrong path is
chosen, he gets disoriented and cannot remember which path it was and the
probabilities remain the same.

What is the expected value of the amount of days he will spend before he exits
the miner?
"""


# %% Import dependencies
import random

# %% Set constants
N = 100_000
p_A = 0.5
p_BB = p_BA = 0.5 * 0.5
d_A = 5
d_BA = 2
d_BB = 1

p = [p_A, p_BA, p_BB]
d = [d_A, d_BA, d_BB]
next_location_map = list(zip([0, 1, 2], ["in", "in", "out"]))


# %% Define simulation functions
def miner_path_sim(days: int = 0, location: str = "in") -> tuple:
    """
    Simulates one stranded miner using recursive logic
    """

    # Base case
    if location == "out":
        return days, location

    # Recursive case
    path_idx, location = random.choices(next_location_map, weights=p, k=1)[0]
    days += d[path_idx]
    return miner_path_sim(days, location)


def expectation(n: int = 100):
    results = [miner_path_sim()[0] for _ in range(n)]
    return sum(results) / len(results)


# %% Run experiment numerous times
if __name__ == "__main__":
    print(expectation(N))
