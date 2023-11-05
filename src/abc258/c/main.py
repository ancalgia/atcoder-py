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
    NQ, S, *rest = case.splitlines()

    N, Q = list(map(int, NQ.split()))

    queries = [list(map(int, x.split())) for x in rest]

    SS = S + S

    indicator = N

    for x in queries:
        if x[0] == 1:
            indicator -= x[1]
        else:
            while indicator < N:
                indicator += N

            indicator -= N

            print(SS[indicator + x[1] - 1])


if __name__ == "__main__":
    main()
