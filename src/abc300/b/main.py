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
# 4 3
# ..#
# ...
# .#.
# ...
# #..
# ...
# .#.
# ...
#     """
# ).strip()


def main():
    HW, *rest = SL(case)

    H, W = IL(HW)

    matrixA = list(map(list, rest[:H]))

    matrixB = list(map(list, rest[H:]))

    doubleB = [x + x for x in matrixB]

    quadroB = doubleB + doubleB

    for sh in range(H + 1):
        pass
        for sw in range(W + 1):
            tgt = quadroB[sh : sh + H]
            tgt = [z[sw : sw + W] for z in tgt]

            isSame = True
            for checkH in range(H):
                if matrixA[checkH] != tgt[checkH]:
                    isSame = False
                    break

            if isSame:
                print("Yes")
                return

    print("No")


if __name__ == "__main__":
    main()
