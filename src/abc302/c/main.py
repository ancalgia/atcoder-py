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
# 4 4
# bbed
# abcd
# abed
# fbed
#     """
# ).strip()


def countDiff(le: str, ri: str) -> int:
    return [x != y for x, y in zip(le, ri)].count(True)


def main():
    NM, *Ss = SL(case)

    allPtn = list(itertools.permutations(Ss))

    for ptn in allPtn:
        pass
        diffs = [countDiff(right, left) for left, right in zip(ptn, ptn[1:])]

        if all([x == 1 for x in diffs]):
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
