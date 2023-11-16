#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


# case: str = "".join([x for x in sys.stdin])


case = "9 20 30"


def main():
    A, B, N = IL(case)

    result = 0

    # loopCount = min(N, B)

    for x in range(1, N + 1):
        tmp = ((A * x) // B) - (A * (x // B))
        print(tmp)
        result = max(tmp, result)

    print(result)
    pass


if __name__ == "__main__":
    main()
