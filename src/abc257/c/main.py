#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# from textwrap import dedent

# case = dedent(
#     """
# 5
# 10101
# 60 45 30 40 80
#     """
# ).strip()


def main():
    N, S, Ws = SL(case)

    N = int(N)

    S = list(S)

    Ws = list(map(int, Ws.split()))

    adults: list[int] = []

    children: list[int] = []

    [adults.append(w) if s == "1" else children.append(w) for s, w in zip(S, Ws)]

    if len(children) == 0 or len(adults) == 0:
        print(N)
        return

    maxChild = max(children)

    minAdult = min(adults)

    if maxChild < minAdult:
        print(N)
        return

    children.sort()
    adults.sort()

    absoluteCount = len([x for x in children if x < minAdult]) + len([x for x in adults if x > maxChild])

    ambChildren = [x for x in children if x >= minAdult]
    ambAdults = [x for x in adults if x <= maxChild]

    ambAll = sorted(ambChildren + ambAdults)

    ambMax = 0

    for x in ambAll:
        tmpA = bisect.bisect_left(ambChildren, x) + (len(ambAdults) - bisect.bisect_left(ambAdults, x))
        tmpB = bisect.bisect_right(ambChildren, x) + (len(ambAdults) - bisect.bisect_right(ambAdults, x))

        ambMax = max(ambMax, max(tmpA, tmpB))

    print(absoluteCount + ambMax)


if __name__ == "__main__":
    main()
