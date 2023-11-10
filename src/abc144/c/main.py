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

# case = "16"


def main():
    N = int(case)

    if N == 1:
        print(0)
        return

    divs = make_divisors(N)

    if len(divs) % 2 == 1:
        result = divs[len(divs) // 2] * 2 - 2
    else:
        result = divs[(len(divs) // 2) - 1] + divs[len(divs) // 2] - 2
    # result = 999999999999999999999999

    pass

    print(result)

    pass


if __name__ == "__main__":
    main()
