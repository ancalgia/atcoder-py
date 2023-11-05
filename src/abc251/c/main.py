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
    N, *Ss = case.splitlines()

    poemAndScores = [x.split() for x in Ss]

    poemSet = set([x[0] for x in poemAndScores])

    maxScore = 0

    maxIdx = 99999999

    for idx, x in enumerate(poemAndScores):
        if x[0] in poemSet:
            poemSet.remove(x[0])

            if maxScore < int(x[1]):
                maxScore = int(x[1])
                maxIdx = idx

    print(maxIdx + 1)


if __name__ == "__main__":
    main()
