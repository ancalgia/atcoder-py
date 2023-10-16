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


def main():
    (H, W), *matrix = IALL(case)

    # changedMatrix = numpy.transpose(numpy.array(matrix))
    changedMatrix = numpy.transpose(matrix)

    for x in changedMatrix:
        print(" ".join(map(str, x)))

    pass


if __name__ == "__main__":
    main()
