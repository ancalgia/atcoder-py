#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# from textwrap import dedent

# case = dedent(
#     """
# 4
# 1937458062
# 1937458062
# 8124690357
# 8124690357
#     """
# ).strip()


def main():
    N, *Ss = SL(case)

    Ss = [list(x) for x in Ss]

    idxListList = [[y.index(key) for y in Ss] for key in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]

    minTime = 10**20
    for x in idxListList:
        sameCounter = collections.Counter(x)

        extraLoop = max([sameCounter[x] - 1 for x in sameCounter])

        if extraLoop == 0:
            lastStop = max(x)
        else:
            topSame = sameCounter.most_common()[0][1]

            lastStop = max([x for x in sameCounter if sameCounter[x] == topSame])

        tmpTime = lastStop + (extraLoop * 10)

        minTime = min([minTime, tmpTime])

    print(minTime)


if __name__ == "__main__":
    main()
