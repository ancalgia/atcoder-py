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
# 0 8 8
# 0 8 8
# 0 8 8
#     """
# ).strip()


def main():
    matrix = IALL(case)

    yokoDiff0 = [right - left for left, right in zip(matrix[0], matrix[0][1:])]
    yokoDiff1 = [right - left for left, right in zip(matrix[1], matrix[1][1:])]
    yokoDiff2 = [right - left for left, right in zip(matrix[2], matrix[2][1:])]

    rot: list[list[int]] = list(zip(*matrix))

    tateDiff0 = [right - left for left, right in zip(rot[0], rot[0][1:])]
    tateDiff1 = [right - left for left, right in zip(rot[1], rot[1][1:])]
    tateDiff2 = [right - left for left, right in zip(rot[2], rot[2][1:])]

    cond = all([yokoDiff0 == yokoDiff1 == yokoDiff2, tateDiff0 == tateDiff1 == tateDiff2])

    print("Yes") if cond else print("No")


if __name__ == "__main__":
    main()
