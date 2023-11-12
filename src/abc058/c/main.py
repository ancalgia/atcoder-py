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
    N, *Ss = SL(case)

    counterList: list[collections.Counter[str]] = []

    setList: list[set[str]] = []

    for s in Ss:
        counterList.append(collections.Counter(s))
        setList.append(set(s))

    caps: set[str] = setList[0]

    for x in setList:
        caps &= x

    capsdict: dict[str, int] = dict()

    for x in caps:
        tmpCount = 999999999999999999
        for y in counterList:
            tmpCount = min(y[x], tmpCount)

        capsdict[x] = tmpCount

    result = [x * capsdict[x] for x in capsdict]

    print("".join(sorted("".join(result))))


if __name__ == "__main__":
    main()
