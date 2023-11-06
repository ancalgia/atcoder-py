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
# -WWW
# L-DD
# LD-W
# LDW-
#     """
# ).strip()


def main():
    N, *matrix = SL(case)

    matrix = list(map(list, matrix))

    matrixB = list(zip(*matrix))

    for x in range(int(N)):
        for y in range(int(N)):
            if matrix[x][y] == "-":
                if matrixB[x][y] != "-":
                    print("incorrect")
                    return

            elif matrix[x][y] == "W":
                if matrixB[x][y] != "L":
                    print("incorrect")
                    return

            elif matrix[x][y] == "L":
                if matrixB[x][y] != "W":
                    print("incorrect")
                    return

            else:
                if matrixB[x][y] != "D":
                    print("incorrect")
                    return

    print("correct")


if __name__ == "__main__":
    main()
