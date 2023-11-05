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

    existCounter = collections.Counter(As).most_common()

    result = 0

    for c1 in existCounter:
        for c2 in existCounter:
            result += ((c1[0] - c2[0]) ** 2) * c1[1] * c2[1]

    print(result // 2)


if __name__ == "__main__":
    main()
