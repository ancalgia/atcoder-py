#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


# 約数の列挙
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


case: str = "".join([x for x in sys.stdin])


def main():
    N = int(case)

    yakusu = make_divisors(N)

    [print(x) for x in yakusu]

    pass


if __name__ == "__main__":
    main()
