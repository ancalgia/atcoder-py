#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on

MOD = 10**9 + 7

case: str = "".join([x for x in sys.stdin])


def main():
    N, M = IL(case)

    if abs(N - M) >= 2:
        print(0)
        return

    inu = math.factorial(N)
    saru = math.factorial(M)

    if N == M:
        print(((((inu % MOD) * (saru % MOD)) % MOD) * 2) % MOD)

    else:
        print(((inu % MOD) * (saru % MOD)) % MOD)


if __name__ == "__main__":
    main()
