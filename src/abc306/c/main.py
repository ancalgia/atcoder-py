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
# 3
# 1 1 3 2 3 2 2 3 1
#     """
# ).strip()
# # 1 3 2


def main():
    (N,), As = IALL(case)

    idxDict: dict[int, list[int]] = dict()

    for x in range(1, N + 1):
        idxDict[x] = []

    # for x in range(1,N+1):

    for idx, x in enumerate(As, 1):
        idxDict[x].append(idx)

    resultList = []

    for x in range(1, N + 1):
        # print(idxDict[x][1])
        resultList.append((idxDict[x][1], x))

    resultList.sort()

    print(*[x[1] for x in resultList])

    pass


if __name__ == "__main__":
    main()
