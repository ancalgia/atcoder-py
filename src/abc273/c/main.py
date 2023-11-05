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
    (N,), As = [list(map(int, x.split())) for x in case.splitlines()]

    revSet = sorted(set(As), reverse=True)

    AsCountDict: dict[int, int] = dict()

    for idx, x in enumerate(revSet):
        AsCountDict[x] = idx

    counts = [AsCountDict[x] for x in As]

    counterDict = dict(collections.Counter(counts))

    pass
    for k in range(N):
        print(counterDict.get(k, 0))


if __name__ == "__main__":
    main()
