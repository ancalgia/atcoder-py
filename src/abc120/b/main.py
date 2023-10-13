#!/usr/bin/env python3


def make_divisors(n: int) -> list[int]:
    lower_divisors: list[int] = []
    upper_divisors: list[int] = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    A, B, K = map(int, input().split())

    divA = make_divisors(A)
    divB = make_divisors(B)

    commons = sorted(set(divA) & set(divB))

    print(commons[-K])


if __name__ == "__main__":
    main()
