from functools import cache


@cache
def f_simplified(n: int):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n % 2 == 1:
        return 0
    if n == 2:
        return 3
    return 4 * f_simplified(n - 2) - f_simplified(n - 4)


@cache
def f(n: int):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n % 2 == 1:
        return 0
    if n == 2:
        return 3
    return 3 * f(n - 2) + 2 * sum(f(n - i) for i in range(4, n + 1, 2))


if __name__ == "__main__":
    for i in range(0, 10_000 + 1):
        assert f(i) == f_simplified(i), f"mismatch at n = {i}"
