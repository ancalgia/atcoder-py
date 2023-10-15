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
    N, As = IALL(case)

    AsSet = set(As)

    Asdict: dict[int, int] = dict()

    for idx, x in enumerate(sorted(AsSet), 1):
        Asdict[x] = idx

    result = []
    for x in As:
        result.append(Asdict[x])

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
