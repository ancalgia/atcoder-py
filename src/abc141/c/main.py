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
    (N, K, Q), *rest = IALL(case)

    Queries = [x[0] for x in rest]

    QCounter = collections.Counter(Queries)

    for x in range(1, N + 1):
        if Q - QCounter[x] >= K:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()
