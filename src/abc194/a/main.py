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
    A, B = IL(case)

    if (A + B) >= 15 and B >= 8:
        print(1)

    elif (A + B) >= 10 and B >= 3:
        print(2)

    elif (A + B) >= 3:
        print(3)
    else:
        print(4)


if __name__ == "__main__":
    main()
