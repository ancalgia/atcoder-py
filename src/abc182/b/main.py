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
    (N,), As = IALL(case)

    if N == 1:
        print(As[0])
        return

    As.sort()

    currMaxGcd = 0

    result = 0

    for x in range(As[-1], 1, -1):
        tmp = 0
        for y in As:
            if y % x == 0:
                tmp += 1

                if currMaxGcd < tmp:
                    currMaxGcd = tmp
                    result = x

    print(result)
    pass


if __name__ == "__main__":
    main()
