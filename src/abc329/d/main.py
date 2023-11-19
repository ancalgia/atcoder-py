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
# 9 8
# 8 8 2 2 8 8 2 2
#     """
# ).strip()


def main():
    (N, M), As = IALL(case)

    pass

    counter: collections.Counter[int] = collections.Counter([])

    # votes  =[]

    # maxvote = 0

    currSelection = (9999999999, 0)

    for a in As:
        if a in counter:
            counter[a] += 1
        else:
            counter[a] = 1

        score = counter[a]

        if score > currSelection[1] or (score == currSelection[1] and a <= currSelection[0]):
            currSelection = (a, score)

        print(currSelection[0])


if __name__ == "__main__":
    main()
