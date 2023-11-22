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
# 3 4 730
# 60 90 120
# 80 150 80 150
#     """
# ).strip()
# # 7


def main():
    (N, M, K), As, Bs = IALL(case)

    aCum: list[int] = []
    bCum: list[int] = []

    tmp = 0
    for x in As:
        tmp += x
        aCum.append(tmp)

    tmp = 0
    for x in Bs:
        tmp += x
        bCum.append(tmp)

    maxBooks = 0

    # Aを読める最大数
    maxA = bisect.bisect_right(aCum, K)

    # print(maxA)
    pass

    for reada in range(maxA, -1, -1):
        nokoriTIme = K - (aCum[reada - 1] if reada else 0)

        bCount = bisect.bisect_right(bCum, nokoriTIme)

        maxBooks = max(maxBooks, reada + bCount)

    print(maxBooks)


if __name__ == "__main__":
    main()
