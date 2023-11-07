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
    AB, S = SL(case)

    A, B = IL(AB)

    if S.count("-") != 1:
        print("No")
        return

    S1, S2 = S.split("-")

    cond = len(S1) == A and len(S2) == B

    print("Yes") if cond else print("No")


if __name__ == "__main__":
    main()
