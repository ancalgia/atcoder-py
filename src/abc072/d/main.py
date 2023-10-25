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
    (N,), Ps = IALL(case)

    contBadCnt = 0
    contBadlist: list[int] = []

    for idx, x in enumerate(Ps, 1):
        if idx == x:
            contBadCnt += 1
        else:
            if contBadCnt != 0:
                contBadlist.append(contBadCnt)
                contBadCnt = 0

    if contBadCnt != 0:
        contBadlist.append(contBadCnt)

    print(sum([math.ceil(x / 2) for x in contBadlist]))


if __name__ == "__main__":
    main()
