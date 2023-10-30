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
    (N, M), *Ks = IALL(case)

    sankaDict: dict[int, set[int]] = dict()

    for x in range(1, N + 1):
        sankaDict[x] = {x}

    for k, *Xs in Ks:
        for x in Xs:
            sankaDict[x].update(Xs)

    for x in sankaDict:
        if len(sankaDict[x]) != N:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
