from collections import Counter


def distribution_of_digital_roots(n):
    roots = Counter(x % 9 for x in range(1, n + 1))
    print(f"1's: {roots[1]} vs. 2's: {roots[2]}")


if __name__ == "__main__":
    distribution_of_digital_roots(1_000_000)
