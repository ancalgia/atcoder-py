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
    S, K, *_ = SL(case)

    K = int(K)

    count1s = 0

    firstElse = ""

    for c in S:
        if c == "1":
            count1s += 1
        else:
            firstElse = c
            break

    print("1") if K <= count1s else print(firstElse)

    pass


if __name__ == "__main__":
    main()
