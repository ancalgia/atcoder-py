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
# 2 2
# 3 1 4 7
# 2 5 9
# 1 3
# 2 1
#     """
# ).strip()


def main():
    (N, Q), *rest = IALL(case)

    tmpAs = rest[:N]

    As = [x[1:] for x in tmpAs]

    Queries = rest[N:]

    for s, k in Queries:
        print(As[s - 1][k - 1])


if __name__ == "__main__":
    main()
