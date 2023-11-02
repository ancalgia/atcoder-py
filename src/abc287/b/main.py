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
# 3 3
# 142857
# 004159
# 071028
# 159
# 287
# 857
#     """
# ).strip()


def main():
    NM, *rest = SL(case)

    N, M = IL(NM)

    Ss = rest[:N]
    Ts = rest[N:]

    result = 0

    for x in Ss:
        if x[3:] in Ts:
            result += 1

    print(result)


if __name__ == "__main__":
    main()
