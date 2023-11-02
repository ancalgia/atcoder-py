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
    (N, M), *ABs = IALL(case)

    losers = set([x[1] for x in ABs])

    maybeSaikyo: list[int] = []

    for x in range(1, N + 1):
        if x not in losers:
            maybeSaikyo.append(x)

    print(maybeSaikyo[0]) if len(maybeSaikyo) == 1 else print(-1)


if __name__ == "__main__":
    main()
