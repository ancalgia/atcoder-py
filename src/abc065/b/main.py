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
    (N,), *As = IALL(case)

    As = [x[0] for x in As]

    light = 1
    result = 0

    pushedSet: set[int] = set()

    while True:
        next = As[light - 1]

        if light in pushedSet:
            print(-1)
            return
        else:
            pushedSet.add(light)

        result += 1
        if next == 2:
            print(result)
            return

        light = next

    pass


if __name__ == "__main__":
    main()
