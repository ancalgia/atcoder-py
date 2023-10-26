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
    A, B, C = IL(case)

    # le = A**C
    # ri = B**C

    isEven = C % 2 == 0

    if any([A == B, abs(A) == B and isEven]):
        print("=")
        return

    if isEven:
        if abs(A) < abs(B):
            print("<")
            return
        else:
            print(">")
            return

    else:
        if A < B:
            print("<")
            return
        else:
            print(">")
            return


if __name__ == "__main__":
    main()
