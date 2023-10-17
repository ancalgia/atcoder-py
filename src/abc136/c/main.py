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
    (N,), Hs = IALL(case)

    current = Hs[0] - 1

    for x in Hs:
        diff = x - current

        if diff <= -1:
            print("No")
            return

        # if diff == -1:
        #     continue

        if diff == 0:
            continue

        if diff == 1:
            continue

        current = x - 1

    print("Yes")


if __name__ == "__main__":
    main()
