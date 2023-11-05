#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def main():
    As = IL(case)

    As.sort()

    diffs = [right - left for left, right in zip(As, As[1:])]

    condition = diffs[0] == diffs[1]

    print("Yes") if condition else print("No")


if __name__ == "__main__":
    main()
