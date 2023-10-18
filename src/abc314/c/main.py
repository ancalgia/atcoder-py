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
    NM, S, C = SL(case)

    N, M = IL(NM)

    Cs = IL(C)

    strList = list(S)

    strColorList = list(zip(strList, Cs))

    deque = collections.deque

    newRevolvers: dict[int, deque[str]] = dict()

    for x in range(1, M + 1):
        newRevolvers[x] = deque()

    for x in strColorList:
        newRevolvers[x[1]].append(x[0])

    for x in newRevolvers:
        newRevolvers[x].rotate(1)
        newRevolvers[x].reverse()

    result: str = ""

    for x in Cs:
        result += newRevolvers[x].pop()

    print(result)


if __name__ == "__main__":
    main()
