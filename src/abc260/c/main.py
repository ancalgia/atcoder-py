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
    N, X, Y = IL(case)

    matrix: list[list[int]] = [[1 if x == 0 else 0, 0] for x in range(N)]

    for idx in range(N - 1):
        matrix[idx + 1][0] += matrix[idx][0]

        matrix[idx][1] += matrix[idx][0] * X

        matrix[idx + 1][0] += matrix[idx][1]

        matrix[idx + 1][1] += matrix[idx][1] * Y

    print(matrix[-1][-1])


if __name__ == "__main__":
    main()
