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
    S = case.rstrip()

    count = 0

    for x in ["a", "t", "c", "o", "d", "e", "r"]:
        idx = S.index(x)
        count += idx
        S = S.replace(x, "")

    print(count)


if __name__ == "__main__":
    main()
