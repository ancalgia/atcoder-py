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
    (H, W), *matrix = IALL(case)

    num2alpha = lambda c: chr(c + 64)

    for x in matrix:
        tmp = ["." if z == 0 else num2alpha(z) for z in x]
        print("".join(tmp))

    pass


if __name__ == "__main__":
    main()
