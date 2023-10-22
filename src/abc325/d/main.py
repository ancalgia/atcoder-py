#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


# case: str = "".join([x for x in sys.stdin])

from textwrap import dedent

case = dedent(
    """
5
1 1
1 1
2 1
1 2
1 4
    """
).strip()

# 5
# 1 1
# 1 1
# 2 1
# 1 2
# 1 4


def main():
    N, *TDs = IALL(case)

    inCounter = collections.Counter([x[0] for x in TDs])
    outCounter = collections.Counter([x[0] + x[1] for x in TDs])

    # inOutCounter = inCounter + outCounter
    # inOutCounter2 = inCounter - outCounter

    hogeDict: dict[int, int] = dict()

    for x in inCounter:
        hogeDict[x] = inCounter[x]

    for x in outCounter:
        if x in hogeDict:
            hogeDict[x] -= outCounter[x]
        else:
            hogeDict[x] = -outCounter[x]

    pass


if __name__ == "__main__":
    main()
