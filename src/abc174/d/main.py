#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import re
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
# 4
# WWRR
#     """
# ).strip()
# 4
# WWRR

# 8
# WRWWRWRR


def main():
    N, S = SL(case)

    if re.search("WR", S) is None:
        print(0)
        return

    wCount = S.count("W")

    dontNeedMoveCount = S[-wCount:].count("W")

    print(wCount - dontNeedMoveCount)


if __name__ == "__main__":
    main()
