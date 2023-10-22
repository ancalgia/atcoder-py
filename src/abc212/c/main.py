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
    (N, M), As, Bs = IALL(case)

    aSet = set(As)
    sortedBs = sorted(Bs)

    small = 999999999999999999

    for a in aSet:
        left = bisect.bisect_left(sortedBs, a)
        # right = bisect.bisect_right(sortedBs, a)

        curr1 = abs(a - (sortedBs[left - 1] if left > 0 else sortedBs[0]))
        curr2 = abs(a - (sortedBs[left] if left < len(sortedBs) else sortedBs[-1]))

        small = min([small, curr1, curr2])

    print(small)


if __name__ == "__main__":
    main()
