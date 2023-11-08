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

    result = 1

    if 0 in As:
        print(0)
        return

    for x in As:
        result *= x
        if result >= 1000000000000000001:
            print(-1)
            return

    print(result)


if __name__ == "__main__":
    main()
