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
# 100000 3
# 7777 AC
# 7777 AC
# 7777 AC
#     """
# ).strip()


def main():
    NM, *PSs = SL(case.rstrip())

    N, M = IL(NM)

    AC = 0

    WADict: dict[int, int] = dict()

    ACSet: set[int] = set()

    for x in PSs:
        p, s = x.split()
        p = int(p)

        if p in ACSet:
            continue

        if s == "AC":
            ACSet.add(p)
            AC += 1
        else:
            if p in WADict:
                WADict[p] += 1
            else:
                WADict[p] = 1

    WA = sum([WADict[x] for x in WADict if x in ACSet])

    print(f"{AC} {WA}")


if __name__ == "__main__":
    main()
