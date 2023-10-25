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
#     """
# ).strip()

# a
# 6
# 2_2_a
# 2_1_b
# 1
# 2_2_c
# 1
# 1

# output:
# (empty)
# expected:
# aabc


def main():
    S, Q, *Queries = SL(case)

    Queries = [x.split() for x in Queries]

    Queries = [(int(x[0]), 0 if x[0] == "1" else int(x[1]), "" if x[0] == "1" else x[2]) for x in Queries]

    frontStr = ""
    backStr = ""

    isReversed = False

    for queri in Queries:
        if queri[0] == 1:
            isReversed = not isReversed

        elif queri[1] == 1:
            if not isReversed:
                frontStr += queri[2]
            else:
                backStr += queri[2]

        else:
            if not isReversed:
                backStr += queri[2]
            else:
                frontStr += queri[2]

    if not isReversed:
        print(frontStr[::-1] + S + backStr)
    else:
        print(backStr[::-1] + S[::-1] + frontStr)

    pass


if __name__ == "__main__":
    main()
