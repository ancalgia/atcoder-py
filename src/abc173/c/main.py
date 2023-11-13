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
# 6 6 8
# ..##..
# .#..#.
# #....#
# ######
# #....#
# #....#
#     """
# ).strip()


def main():
    HWK, *matrix = SL(case)

    H, W, K = IL(HWK)

    matrix = [list(x) for x in matrix]

    HPtn = list(itertools.product(*[[True, False] for x in range(H)]))
    WPtn = list(itertools.product(*[[True, False] for x in range(W)]))

    HWPtn = list(itertools.product(HPtn, WPtn))

    result = 0

    for hp, wp in HWPtn:
        tmp = 0

        for x in range(H):
            if hp[x] == False:
                continue

            for y in range(W):
                if wp[y] == False:
                    continue

                if matrix[x][y] == "#":
                    tmp += 1

        if tmp == K:
            result += 1

    print(result)

    pass


if __name__ == "__main__":
    main()
