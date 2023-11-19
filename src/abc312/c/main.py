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
    (N, M), As, Bs = IALL(case)

    As.sort()
    Bs.sort()

    for x in sorted(set(As + Bs)):
        sellers = bisect.bisect_right(As, x)
        buyers = M - bisect.bisect_left(Bs, x)

        if sellers >= buyers:
            print(x)
            return

        sellers2 = bisect.bisect_right(As, x + 1)
        buyers2 = M - bisect.bisect_left(Bs, x + 1)

        if sellers2 >= buyers2:
            print(x + 1)
            return


if __name__ == "__main__":
    main()
