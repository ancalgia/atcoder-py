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
# ##.......
# ##.......
# .........
# .......#.
# .....#...
# ........#
# ......#..
# .........
# .........
#     """
# ).strip()


def main():
    martix = SL(case)

    pawnSet: list[tuple[int, int]] = []

    for x in range(9):
        for y in range(9):
            if martix[x][y] == "#":
                pawnSet.append((x, y))

    allHens = list(itertools.permutations(pawnSet, 2))

    resultSet: set[
        tuple[
            tuple[int, int],
            tuple[int, int],
            tuple[int, int],
            tuple[int, int],
        ]
    ] = set()

    pass

    for A, B in allHens:
        diff1 = B[0] - A[0]
        diff2 = B[1] - A[1]

        maybeD = (A[0] + diff2, A[1] - diff1)
        maybeC = (B[0] + diff2, B[1] - diff1)

        if maybeC in pawnSet and maybeD in pawnSet:
            hoge = tuple(sorted([A, B, maybeC, maybeD]))
            resultSet.add(hoge)

    print(len(resultSet))


if __name__ == "__main__":
    main()
