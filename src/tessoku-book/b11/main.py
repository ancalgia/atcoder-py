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
# 1 3 3 3 1
# 2
# 4
# 3
# """
# ).strip()


def main():
    (N,), As, (Q,), *Xs = IALL(case)

    sortedAs = sorted(As)

    for x in Xs:
        idx = bisect.bisect_left(sortedAs, x[0])

        print(idx)

    pass


if __name__ == "__main__":
    main()
