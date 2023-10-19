#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys

import numpy


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
# 0101
# 1101
# 1111
# 0000
#     """
# ).strip()


def main():
    N, *M = SL(case)

    N = int(N)

    matrix: list[list[int]] = []

    for x in M:
        matrix.append(list(map(int, list(x))))

    currFrame = matrix[0][0:-1].copy()
    matrix = numpy.rot90(matrix)

    currFrame.extend(matrix[0][0:-1].copy())
    matrix = numpy.rot90(matrix)

    currFrame.extend(matrix[0][0:-1].copy())
    matrix = numpy.rot90(matrix)

    currFrame.extend(matrix[0][0:-1].copy())
    matrix = numpy.rot90(matrix)

    currFrame = [currFrame[-1]] + currFrame[0:-1]

    splitted = numpy.array_split(currFrame, 4)

    for x in range(N - 1):
        matrix[0][x] = splitted[0][x]
    matrix = numpy.rot90(matrix)

    for x in range(N - 1):
        matrix[0][x] = splitted[1][x]
    matrix = numpy.rot90(matrix)

    for x in range(N - 1):
        matrix[0][x] = splitted[2][x]
    matrix = numpy.rot90(matrix)

    for x in range(N - 1):
        matrix[0][x] = splitted[3][x]
    matrix = numpy.rot90(matrix)

    for row in matrix:
        print("".join([str(x) for x in row]))


if __name__ == "__main__":
    main()
