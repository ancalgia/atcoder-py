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
    (N,), Ls = IALL(case)

    Ls.sort()

    result = 0

    for x in range(N):
        bar1 = Ls[x]

        for y in range(x + 1, N):
            bar2 = Ls[y]

            ableMax = bar1 + bar2

            tgt = Ls[y + 1 :]

            ableCnt = bisect.bisect_left(tgt, ableMax)

            result += ableCnt

    print(result)


if __name__ == "__main__":
    main()
