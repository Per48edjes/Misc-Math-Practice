import argparse
import math


def f(n: int) -> float:
    x = 0
    for _ in range(n):
        x = math.sqrt(4 + 3 * x)
    return x


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Return the nth number in the sequence"
    )
    parser.add_argument(
        "-n",
        type=int,
        nargs="?",
        default=100,
        help="an integer for the desired stopping index",
    )
    args = parser.parse_args()
    print(f"index {args.n} => {f(args.n)}")
