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
# 8 3
# ACACTACG
# 3 7
# 2 3
# 1 8
#     """
# ).strip()


def main():
    NQ, S, *Queries = SL(case)

    Queries = [IL(x) for x in Queries]

    AClist = [left == "A" and right == "C" for left, right in zip(S, S[1:])]

    cum: list[int] = [0]

    tmp = 0

    for x in AClist:
        if x:
            tmp += 1

        cum.append(tmp)

    for le, ri in Queries:
        print(cum[ri - 1] - cum[le - 1])


if __name__ == "__main__":
    main()
