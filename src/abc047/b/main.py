#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# from textwrap import dedent

# case = dedent(
#     """
# 1 1 0
# 2 2 2
#     """
# ).strip()


def main():
    (W, H, N), *XYAs = IALL(case)

    leftW = 0
    rightW = W
    bottomH = 0
    topH = H

    for x, y, a in XYAs:
        if a == 1:
            leftW = max(leftW, x)

        elif a == 2:
            rightW = min(rightW, x)

        elif a == 3:
            bottomH = max(bottomH, y)

        else:
            topH = min(topH, y)

    if rightW - leftW <= 0 or topH - bottomH <= 0:
        print(0)
        return

    print(max(0, (rightW - leftW) * (topH - bottomH)))


if __name__ == "__main__":
    main()
