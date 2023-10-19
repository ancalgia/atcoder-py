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


def main():
    S = case

    bIndex = [x.start() for x in re.finditer("B", S)]

    if bIndex[0] % 2 == bIndex[1] % 2:
        print("No")
        return

    rIndex = [x.start() for x in re.finditer("R", S)]
    kIndex = [x.start() for x in re.finditer("K", S)]

    if not (rIndex[0] < kIndex[0] < rIndex[1]):
        print("No")
        return

    print("Yes")


if __name__ == "__main__":
    main()
