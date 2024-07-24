def main():
    for n in range(0, 100 + 1, 2):
        if n & (n - 1) == 0:
            continue
        print(f"{n=} {2**n + 1=}")


if __name__ == "__main__":
    main()
