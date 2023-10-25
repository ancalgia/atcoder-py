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
    (N,), *XYs = IALL(case)

    allPtn = itertools.combinations(XYs, 3)

    for A, B, C in allPtn:
        if (A[1] - B[1]) == 0 or (A[1] - C[1]) == 0:
            if (A[1] - B[1]) == (A[1] - C[1]):
                print("Yes")
                return
            else:
                continue

        if (A[0] - B[0]) / (A[1] - B[1]) == (A[0] - C[0]) / (A[1] - C[1]):
            print("Yes")
            return

    print("No")
    pass


if __name__ == "__main__":
    main()
