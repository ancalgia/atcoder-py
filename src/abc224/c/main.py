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
# 4
# 0 1
# 1 3
# 1 1
# -1 -1
#     """
# ).strip()


# from textwrap import dedent

# case = dedent(
#     """
# 20
# 224 433
# 987654321 987654321
# 2 0
# 6 4
# 314159265 358979323
# 0 0
# -123456789 123456789
# -1000000000 1000000000
# 124 233
# 9 -6
# -4 0
# 9 5
# -7 3
# 333333333 -333333333
# -9 -1
# 7 -10
# -1 5
# 324 633
# 1000000000 -1000000000
# 20 0
#     """
# ).strip()
# # 1124


def main():
    (N,), *XYs = IALL(case)

    result = 0

    for aIdx in range(N):
        ax, ay = XYs[aIdx]
        for bIdx in range(aIdx + 1, N):
            bx, by = XYs[bIdx]

            isABInf = bx - ax == 0

            for cIdx in range(bIdx + 1, N):
                cx, cy = XYs[cIdx]

                isACInf = cx - ax == 0

                if isACInf:
                    if isABInf:
                        continue
                    else:
                        result += 1
                        continue
                slopeAB = (by - ay) * (cx - ax)
                slopeAC = (cy - ay) * (bx - ax)
                if slopeAB != slopeAC:
                    result += 1
                else:
                    pass

    print(result)


if __name__ == "__main__":
    main()
