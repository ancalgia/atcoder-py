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
    (N, D, P), Fs = [list(map(int, x.split())) for x in case.splitlines()]

    sortedFs = sorted(Fs, reverse=True)

    segmentTotal: list[int] = []

    ticketCount = 0

    for idx, x in enumerate(sortedFs, 1):
        segmentTotal.append(x)

        if idx % D == 0 or idx == len(sortedFs):
            if sum(segmentTotal) >= P:
                ticketCount += 1

                segmentTotal.clear()
            else:
                break

    unuseDays = sortedFs[ticketCount * D :]

    print(ticketCount * P + sum(unuseDays))


if __name__ == "__main__":
    main()
