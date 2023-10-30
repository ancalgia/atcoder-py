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

    strA = str(A).zfill(30)
    strB = str(B).zfill(30)

    for a, b in zip(strA, strB):
        if int(a) + int(b) >= 10:
            print("Hard")
            return

    print("Easy")


if __name__ == "__main__":
    main()
