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
# 4 10
# 1 2 3 4
# """
# ).strip()


def main():
    (N, K), As = IALL(case)

    shortestprinter = min(As)

    # Klist = [x for x in range(K * shortestprinter)]

    minTime = 0

    maxTime = K * shortestprinter

    while True:
        if minTime == maxTime:
            print(minTime)
            return

        center = (minTime + maxTime) // 2
        maisu = sum([center // x for x in As])

        # separator = int(len(Klist) / 2)

        # maisu = sum([Klist[separator] // x for x in As])

        if maisu > K:
            maxTime = center
        elif maisu < K:
            minTime = center + 1
        else:
            maxTime -= 1
    pass


if __name__ == "__main__":
    main()
