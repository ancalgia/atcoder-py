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
    N = int(case)

    allSum = ((1 + N) * N) // 2

    fizzSum = sum([x for x in range(1, N + 1) if x % 3 == 0])

    buzzSum = sum([x for x in range(1, N + 1) if x % 5 == 0])

    fibuSum = sum([x for x in range(1, N + 1) if x % 15 == 0])

    print(allSum - fizzSum - buzzSum + fibuSum)

    pass


if __name__ == "__main__":
    main()
