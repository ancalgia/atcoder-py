#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


sys.setrecursionlimit(10**9)

case: str = "".join([x for x in sys.stdin])


already_vitsited: set[int] = set([1])

fromCityDict: dict[int, int] = {}

routeDict: dict[int, list[int]] = {}


# trace: list[int] = []
trace: collections.deque[int] = collections.deque()


def walk(curr: int):
    trace.append(curr)

    if len(routeDict[curr]) == 0:
        if curr == 1:
            print(*trace)
            exit()
        else:
            walk(fromCityDict[curr])

    while True:
        if len(routeDict[curr]) == 0:
            if curr == 1:
                print(*trace)
                exit()
            else:
                walk(fromCityDict[curr])

        hoge = heapq.heappop(routeDict[curr])

        if hoge not in already_vitsited:
            already_vitsited.add(hoge)
            if hoge not in fromCityDict:
                fromCityDict[hoge] = curr
            walk(hoge)


def main():
    (N,), *ABs = IALL(case)

    # print(*ABs)

    for a, b in ABs:
        if a in routeDict:
            heapq.heappush(routeDict[a], b)

        else:
            routeDict[a] = [b]
            heapq.heapify(routeDict[a])

        if b in routeDict:
            heapq.heappush(routeDict[b], a)
        else:
            routeDict[b] = [a]
            heapq.heapify(routeDict[a])

    walk(1)

    pass


if __name__ == "__main__":
    main()
