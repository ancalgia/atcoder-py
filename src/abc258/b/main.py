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
# 8564
# 6856
# 7847
# 8976
#     """
# ).strip()  # 9885


def main():
    N, *matrix = SL(case)

    N = int(N)

    matrix = [list(map(int, x)) for x in matrix]

    maxNum = max([max(x) for x in matrix])

    startList: list[tuple[int, int]] = []

    for x in range(N):
        for y in range(N):
            if matrix[x][y] == maxNum:
                startList.append((x, y))

    double = [x + x for x in matrix]

    quadro = double + double

    resultNums = 0

    for sx, sy in startList:
        tmpNumsNaname: list[int] = []
        for i in range(N):
            tmpNumsNaname.append(quadro[sx + i][sy + i])

        tmpStr = "".join(map(str, tmpNumsNaname))
        greater = max([int(tmpStr), int(tmpStr[0] + tmpStr[1:][::-1])])
        resultNums = max([resultNums, greater])

        if all([x == maxNum for x in tmpNumsNaname]):
            print(int(tmpStr))
            return

    for sx, sy in startList:
        tmpNumsNaname2: list[int] = []
        for i in range(N):
            tmpNumsNaname2.append(quadro[sx + i][sy - i])

        tmpStr = "".join(map(str, tmpNumsNaname2))
        greater = max([int(tmpStr), int(tmpStr[0] + tmpStr[1:][::-1])])
        resultNums = max([resultNums, greater])

        if all([x == maxNum for x in tmpNumsNaname2]):
            print(int(tmpStr))
            return

    for sx, sy in startList:
        tmpNumsYoko: list[int] = []
        for i in range(N):
            tmpNumsYoko.append(quadro[sx + i][sy])

        tmpStr = "".join(map(str, tmpNumsYoko))
        greater = max([int(tmpStr), int(tmpStr[0] + tmpStr[1:][::-1])])
        resultNums = max([resultNums, greater])

        if all([x == maxNum for x in tmpNumsYoko]):
            print(int(tmpStr))
            return

    for sx, sy in startList:
        tmpNumsTate: list[int] = []
        for i in range(N):
            tmpNumsTate.append(quadro[sx][sy + i])

        tmpStr = "".join(map(str, tmpNumsTate))
        greater = max([int(tmpStr), int(tmpStr[0] + tmpStr[1:][::-1])])
        resultNums = max([resultNums, greater])

        if all([x == maxNum for x in tmpNumsTate]):
            print(int(tmpStr))
            return

    print(resultNums)

    pass


if __name__ == "__main__":
    main()
