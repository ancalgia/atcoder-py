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
    N, *rest = SL(case)

    N = int(N)

    blues = rest[:N]

    M = int(rest[N])

    reds = rest[N + 1 :]

    blueCounter = collections.Counter(blues)
    redCounter = collections.Counter(reds)

    result = 0

    for x in blueCounter:
        tmp = blueCounter[x] - redCounter[x]

        if tmp > 0:
            result = max([tmp, result])

    print(result)


if __name__ == "__main__":
    main()
