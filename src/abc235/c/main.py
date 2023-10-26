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
    (N, Q), As, *Queries = IALL(case)

    AsDict: dict[int, list[int]] = dict()

    for idx, a in enumerate(As, 1):
        if a in AsDict:
            AsDict[a].append(idx)
        else:
            AsDict[a] = [idx]

    for q in Queries:
        if q[0] in AsDict:
            if len(AsDict[q[0]]) >= q[1]:
                print(AsDict[q[0]][q[1] - 1])
            else:
                print(-1)

        else:
            print(-1)


if __name__ == "__main__":
    main()
