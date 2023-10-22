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
    (N,), *LRs = IALL(case)

    plusMinusDict: dict[int, int] = dict()

    for le, ri in LRs:
        if le in plusMinusDict:
            plusMinusDict[le] += 1
        else:
            plusMinusDict[le] = 1

        if ri in plusMinusDict:
            plusMinusDict[ri] -= 1
        else:
            plusMinusDict[ri] = -1

    hoge = sorted(plusMinusDict)

    currentNum = 0

    result: list[list[int | None]] = []

    result.append([hoge[0], None])

    for x in hoge:
        if result[-1][1] is not None:
            result.append([x, None])

        currentNum += plusMinusDict[x]

        if currentNum == 0:
            result[-1][1] = x

    [print(*x) for x in result]


if __name__ == "__main__":
    main()
