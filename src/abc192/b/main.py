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
    S, *_ = SL(case)

    oddStr = "".join([x for idx, x in enumerate(S) if idx % 2 == 0])
    evenStr = "".join([x for idx, x in enumerate(S) if idx % 2 == 1])

    if oddStr == oddStr.lower() and evenStr == evenStr.upper():
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
