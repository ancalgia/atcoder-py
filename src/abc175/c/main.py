#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def main():
    X, K, D = IL(case)

    # isOdd = K % 2 == 1

    maxDist = K * D

    isReachable = abs(X) <= maxDist

    if not isReachable:
        print((abs(X)) - maxDist)
        return

    else:
        d, m = divmod(abs(X), D)

        rest = K - d

        if rest % 2 == 0:
            print(abs(m))
            return
        else:
            print(abs(m - D))
            return


if __name__ == "__main__":
    main()
