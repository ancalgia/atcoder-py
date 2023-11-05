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
    S, *_ = case.splitlines()

    doubleS = S + S

    strings: list[str] = []

    for x in range(len(S)):
        strings.append(doubleS[x : x + len(S)])

    # strSet = set(strings)

    strings.sort()

    first = strings[0]
    last = strings[-1]

    print(first)
    print(last)


if __name__ == "__main__":
    main()
