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
    (N, M, X), *CAs = IALL(case)

    pass

    allPtn = list(itertools.product(*[[True, False] for x in range(N)]))

    CAs = [(c, x) for c, *x in CAs]

    minPrice = 99999999999999999999

    for ptn in allPtn:
        tmpCAs = [x for p, x in zip(ptn, CAs) if p == True]

        tmpPrice = 0

        tmpSkills = [0 for _ in range(M)]

        for c, a in tmpCAs:
            tmpPrice += c
            for idx in range(M):
                tmpSkills[idx] += a[idx]

        if all([z >= X for z in tmpSkills]):
            minPrice = min([minPrice, tmpPrice])

    if minPrice == 99999999999999999999:
        print(-1)
    else:
        print(minPrice)


if __name__ == "__main__":
    main()
