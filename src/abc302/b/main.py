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
# 6 6
# vgxgpu
# amkxks
# zhkbpp
# hykink
# esnuke
# zplvfj
#     """
# ).strip()


def main():
    HW, *matrix = SL(case)

    H, W = IL(HW)

    matrix = list(map(list, matrix))

    startList: list[tuple[int, int]] = []

    for h in range(H):
        for w in range(W):
            if matrix[h][w] == "s":
                startList.append((h, w))

    pass

    for sH, sW in startList:
        maybeSnukeList = [
            [(sH, sW), (sH + 1, sW), (sH + 2, sW), (sH + 3, sW), (sH + 4, sW)],
            [(sH, sW), (sH + 1, sW + 1), (sH + 2, sW + 2), (sH + 3, sW + 3), (sH + 4, sW + 4)],
            [(sH, sW), (sH, sW + 1), (sH, sW + 2), (sH, sW + 3), (sH, sW + 4)],
            [(sH, sW), (sH - 1, sW + 1), (sH - 2, sW + 2), (sH - 3, sW + 3), (sH - 4, sW + 4)],
            [(sH, sW), (sH - 1, sW), (sH - 2, sW), (sH - 3, sW), (sH - 4, sW)],
            [(sH, sW), (sH - 1, sW - 1), (sH - 2, sW - 2), (sH - 3, sW - 3), (sH - 4, sW - 4)],
            [(sH, sW), (sH, sW - 1), (sH, sW - 2), (sH, sW - 3), (sH, sW - 4)],
            [(sH, sW), (sH + 1, sW - 1), (sH + 2, sW - 2), (sH + 3, sW - 3), (sH + 4, sW - 4)],
        ]

        for maybe in maybeSnukeList:
            if any(
                [
                    maybe[-1][0] < 0,
                    H <= maybe[-1][0],
                    maybe[-1][1] < 0,
                    W <= maybe[-1][1],
                ]
            ):
                continue

            if all(
                [
                    matrix[maybe[0][0]][maybe[0][1]] == "s",
                    matrix[maybe[1][0]][maybe[1][1]] == "n",
                    matrix[maybe[2][0]][maybe[2][1]] == "u",
                    matrix[maybe[3][0]][maybe[3][1]] == "k",
                    matrix[maybe[4][0]][maybe[4][1]] == "e",
                ]
            ):
                for x in maybe:
                    print(f"{x[0]+1} {x[1]+1}")
                return


if __name__ == "__main__":
    main()
