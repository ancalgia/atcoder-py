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
    (N, M), *rest = IALL(case)

    bulbs: list[list[int]] = []

    for x in range(M):
        bulbs.append(rest[x][1:])

    setting = rest[-1]

    allPtn: list[tuple[tuple[bool, int], ...]] = list(
        itertools.product(*[[(True, x + 1), (False, x + 1)] for x in range(N)])
    )

    result = 0

    for ptn in allPtn:
        allOn = True

        ons = [x[1] for x in ptn if x[0]]

        for idx, b in enumerate(bulbs, 1):
            count = len([z for z in b if z in ons])
            if count % 2 != setting[idx - 1]:
                allOn = False
                break

        if allOn:
            result += 1

    print(result)


if __name__ == "__main__":
    main()
