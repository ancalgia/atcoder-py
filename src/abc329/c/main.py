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
    N, S = SL(case)

    N = int(N)

    dicts: dict[str, int] = dict()

    lastStr = ""

    tmpCount = 0

    for c in S:
        if c != lastStr:
            lastStr = c
            tmpCount = 1
            if c not in dicts:
                dicts[c] = tmpCount

        else:
            tmpCount += 1

            dicts[c] = max(dicts[c], tmpCount)

    result = sum([dicts[x] for x in dicts])

    print(result)


if __name__ == "__main__":
    main()
