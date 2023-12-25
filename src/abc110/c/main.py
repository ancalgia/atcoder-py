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
    S, T = SL(case)

    SList = list(S)
    TList = list(T)

    Sidxes: list[list[int]] = []
    while True:
        if len(SList) == 0:
            break
        tgt = SList[0]
        Sidxes.append([idx for idx, x in enumerate(SList) if x == tgt])
        SList = [x for x in SList if x != tgt]

    Tidxes: list[list[int]] = []
    while True:
        if len(TList) == 0:
            break
        tgt = TList[0]
        Tidxes.append([idx for idx, x in enumerate(TList) if x == tgt])
        TList = [x for x in TList if x != tgt]

    for si, ti in zip(Sidxes, Tidxes):
        if si != ti:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
