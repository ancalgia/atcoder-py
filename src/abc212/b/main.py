#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def isStrong(le: int, ri: int) -> bool:
    if ri - le == 1 or le == 9 and ri == 0:
        return False
    return True


def main():
    A, B, C, D = map(int, list(str(case.rstrip())))

    if A == B == C == D:
        print("Weak")
        return

    if not isStrong(A, B) and not isStrong(B, C) and not isStrong(C, D) and not isStrong(A, B):
        print("Weak")
        return

    print("Strong")

    pass


if __name__ == "__main__":
    main()
