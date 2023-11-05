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
# 5 5
# 1
# 2
# 3
# 4
# 5
#     """
# ).strip()
# # 1 2 3 5 4


def main():
    (N, Q), *Xs = IALL(case)

    Xs = [x[0] for x in Xs]

    numPosDict: dict[int, int] = dict()
    posNumList: list[int] = [x for x in range(N + 1)]

    for x in range(1, N + 1):
        numPosDict[x] = x

    pass

    for x in Xs:
        me = numPosDict[x]

        if me == N:
            he = posNumList[me - 1]

            numPosDict[x] -= 1

            numPosDict[he] += 1

            posNumList[me], posNumList[me - 1] = posNumList[me - 1], posNumList[me]

            # hoge = next(filter(lambda x: x[1] == 1, numPosDict.items()))
            # numPosDict[hoge[0]] = N

            # numPosDict[x] = 1

        else:
            he = posNumList[me + 1]

            numPosDict[x] += 1

            numPosDict[he] -= 1

            posNumList[me], posNumList[me + 1] = posNumList[me + 1], posNumList[me]

            # numPosDict[posNumList[x] + 1] -= 1
            # numPosDict[x] += 1

            # posNumList[x], posNumList[x + 1] = posNumList[x + 1], posNumList[x]

        pass

    print(*posNumList[1:])

    pass


if __name__ == "__main__":
    main()
