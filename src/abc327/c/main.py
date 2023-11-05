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
    matrix = IALL(case)

    allSet = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    for x in matrix:
        if set(x) != allSet:
            print("No")
            return

    for x in zip(*matrix):
        # if sum(x) != 45:
        if set(x) != allSet:
            print("No")
            return

    if (
        set(
            [
                matrix[0][0],
                matrix[0][1],
                matrix[0][2],
                matrix[1][0],
                matrix[1][1],
                matrix[1][2],
                matrix[2][0],
                matrix[2][1],
                matrix[2][2],
            ]
        )
        != allSet
    ):
        print("No")
        return

    if (
        set(
            [
                matrix[3][0],
                matrix[3][1],
                matrix[3][2],
                matrix[4][0],
                matrix[4][1],
                matrix[4][2],
                matrix[5][0],
                matrix[5][1],
                matrix[5][2],
            ]
        )
        != allSet
    ):
        print("No")
        return

    if (
        set(
            [
                matrix[6][0],
                matrix[6][1],
                matrix[6][2],
                matrix[7][0],
                matrix[7][1],
                matrix[7][2],
                matrix[8][0],
                matrix[8][1],
                matrix[8][2],
            ]
        )
        != allSet
    ):
        print("No")
        return

    ##################
    if (
        set(
            [
                matrix[0][3],
                matrix[0][4],
                matrix[0][5],
                matrix[1][3],
                matrix[1][4],
                matrix[1][5],
                matrix[2][3],
                matrix[2][4],
                matrix[2][5],
            ]
        )
        != allSet
    ):
        print("No")
        return

    if (
        set(
            [
                matrix[3][3],
                matrix[3][4],
                matrix[3][5],
                matrix[4][3],
                matrix[4][4],
                matrix[4][5],
                matrix[5][3],
                matrix[5][4],
                matrix[5][5],
            ]
        )
        != allSet
    ):
        print("No")
        return

    if (
        set(
            [
                matrix[6][3],
                matrix[6][4],
                matrix[6][5],
                matrix[7][3],
                matrix[7][4],
                matrix[7][5],
                matrix[8][3],
                matrix[8][4],
                matrix[8][5],
            ]
        )
        != allSet
    ):
        print("No")
        return
    ##################
    if (
        set(
            [
                matrix[0][6],
                matrix[0][7],
                matrix[0][8],
                matrix[1][6],
                matrix[1][7],
                matrix[1][8],
                matrix[2][6],
                matrix[2][7],
                matrix[2][8],
            ]
        )
        != allSet
    ):
        print("No")
        return

    if (
        set(
            [
                matrix[3][6],
                matrix[3][7],
                matrix[3][8],
                matrix[4][6],
                matrix[4][7],
                matrix[4][8],
                matrix[5][6],
                matrix[5][7],
                matrix[5][8],
            ]
        )
        != allSet
    ):
        print("No")
        return

    if (
        set(
            [
                matrix[6][6],
                matrix[6][7],
                matrix[6][8],
                matrix[7][6],
                matrix[7][7],
                matrix[7][8],
                matrix[8][6],
                matrix[8][7],
                matrix[8][8],
            ]
        )
        != allSet
    ):
        print("No")
        return

    print("Yes")


if __name__ == "__main__":
    main()
