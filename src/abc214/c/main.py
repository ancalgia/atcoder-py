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
    (N,), Ss, Ts = IALL(case)

    timeDict: dict[int, list[int]] = dict()

    for idx in range(1, N + 1):
        timeDict[idx] = [Ss[idx - 1], Ts[idx - 1]]

    STs: collections.deque[list[int]] = collections.deque()

    [STs.append([Ss[x], Ts[x]]) for x in range(N)]

    while True:
        current = tuple(x[1] for x in STs)

        newdq: collections.deque[list[int]] = collections.deque()

        # for x in range(N):

        #     tmp =

        #     Ss[x] = min([Ss[x-1]+,])

    time = 0

    pass


if __name__ == "__main__":
    main()
