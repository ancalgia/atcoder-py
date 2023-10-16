#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def getscore(li: list[int]) -> int:
    return sum(sorted(li)[1:-1])


def main():
    (N, X), As = IALL(case)

    sortedAs = sorted(As)

    min = 0
    max = X

    if getscore(sortedAs + [X]) < X:
        print(-1)
        return

    while True:
        if min == max:
            print(min)
            return

        tgt = (min + max) // 2

        score = getscore(sortedAs + [tgt])

        if score > X:
            if abs(min - max) == 1:
                max -= 1
            else:
                max = tgt
        elif score < X:
            if abs(min - max) == 1:
                min += 1
            else:
                min = tgt
        else:
            if min == max:
                print(min)
                return
            else:
                max -= 1


if __name__ == "__main__":
    main()
