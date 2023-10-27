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
    P, Q = case.split()

    # 点A と点B の距離は3
    # 点B と点C の距離は1
    # 点C と点D の距離は4
    # 点D と点E の距離は1
    # 点E と点F の距離は5
    # 点F と点G の距離は9
    posDict = {"A": 0, "B": 3, "C": 4, "D": 8, "E": 9, "F": 14, "G": 23}

    print(abs(posDict[P] - posDict[Q]))


if __name__ == "__main__":
    main()
