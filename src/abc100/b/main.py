#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "2 100"


def main():
    D, N = IL(case)

    if N != 100:
        print(str(N) + "00" * D)

    else:
        print(int(str(N + 1) + "00" * D))


if __name__ == "__main__":
    main()
