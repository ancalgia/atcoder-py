#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "1"


def main():
    N = int(case)

    # cond = N not in [1, 2, 4, 8, 16, 32]

    cond = 2**N > N**2

    print("Yes") if cond else print("No")


if __name__ == "__main__":
    main()
