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
    (N, M), *PCFFFs = IALL(case)

    itemList: list[tuple[int, int, set[int]]] = []

    for idx, x in enumerate(PCFFFs):
        itemList.append((idx, x[0], set(x[2:])))

    for idx, x in enumerate(itemList):
        if len(x[2]) == 99:
            pass

        maybeUppers = [
            z
            for z in itemList
            if all(
                [
                    x[0] != z[0],
                    any(
                        [
                            x[1] >= z[1] and len(x[2]) < len(z[2]),
                            x[1] > z[1] and len(x[2]) <= len(z[2]),
                        ]
                    ),
                ]
            )
        ]

        for m in maybeUppers:
            if x[2] <= m[2]:
                print("Yes")
                return

    print("No")


if __name__ == "__main__":
    main()
