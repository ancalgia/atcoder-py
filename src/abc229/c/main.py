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
    (N, W), *ABs = IALL(case)

    ABs.sort(reverse=True)

    rest = W

    result = 0

    for a, b in ABs:
        if rest >= b:
            rest -= b
            result += a * b

        else:
            result += rest * a
            print(result)
            return

    print(result)


if __name__ == "__main__":
    main()
