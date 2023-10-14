#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, numpy, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def main():
    N, *STs = SL(case)

    STs = [x.split() for x in STs]

    allNames = itertools.chain.from_iterable(STs)

    counter = collections.Counter(allNames)

    for st in STs:
        if (counter.get(st[0]) == 1 or counter.get(st[1]) == 1) or (st[0] == st[1] and counter.get(st[1]) == 2):
            continue

        print("No")
        return

    print("Yes")


if __name__ == "__main__":
    main()
