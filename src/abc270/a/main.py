#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "7 7"


def main():
    A, B = IL(case)

    is1 = A % 2 == 1 or B % 2 == 1
    is2 = A in [2, 3, 6, 7] or B in [2, 3, 6, 7]
    is4 = A >= 4 or B >= 4

    print((1 if is1 else 0) + (2 if is2 else 0) + (4 if is4 else 0))


if __name__ == "__main__":
    main()
