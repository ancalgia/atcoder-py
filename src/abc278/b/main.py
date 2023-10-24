#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "19 57"


def main():
    H, M = IL(case)

    currentH = H
    currentM = M

    while True:
        HStr = str(currentH).zfill(2)
        MStr = str(currentM).zfill(2)

        changedH = HStr[0] + MStr[0]
        changedM = HStr[1] + MStr[1]

        if int(changedH) <= 23 and int(changedM) <= 59:
            print(f"{int(HStr)} {int(MStr)}")
            return

        if currentM != 59:
            currentM += 1
        else:
            if currentH != 23:
                currentH += 1
            else:
                currentH = 0
            currentM = 0

    pass


if __name__ == "__main__":
    main()
