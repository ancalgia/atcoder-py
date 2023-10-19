#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "20"


def main():
    N = int(case)

    count = N

    for x in range(1, N + 1):
        if "7" in str(x) or "7" in oct(x):
            count -= 1

    print(count)


if __name__ == "__main__":
    main()
