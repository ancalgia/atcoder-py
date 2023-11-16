#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

MOD = 10**9 + 7


def main():
    (N, M), *As = IALL(case)

    As = [x[0] for x in As]

    diffs = [right - left for left, right in zip(As, As[1:])]

    As = set(As)

    if 1 in diffs:
        print(0)
        return

    dp = [0, 1]

    for x in range(1, N + 1):
        if x in As:
            dp.append(0)

        else:
            dp.append((dp[-1] + dp[-2]) % MOD)

    print(dp[-1])


if __name__ == "__main__":
    main()
