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
    (N, K), *ABs = IALL(case)

    left = 1
    right = max([x[0] for x in ABs]) + 100

    result = 9999999999999999999999

    sortedABs = sorted(ABs)

    while True:
        if left == right:
            print(result)
            return

        tgt = (right + left) // 2

        medicines = sum([x[1] for x in sortedABs if x[0] >= tgt])

        if medicines <= K:
            result = min([result, tgt])

            if right == tgt:
                right -= 1
            else:
                right = tgt

        else:
            if left == tgt:
                left += 1
            else:
                left = tgt

    pass


if __name__ == "__main__":
    main()
