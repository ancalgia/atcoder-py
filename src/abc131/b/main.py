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
    NL, *_ = SL(case)

    N, L = list(map(int, NL.split()))

    tasteSet = set([x + L - 1 for x in range(1, N + 1)])

    result = min(tasteSet, key=abs)

    tasteSet.remove(result)

    print(sum(tasteSet))


if __name__ == "__main__":
    main()
