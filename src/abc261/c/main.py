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
    N, *As = case.splitlines()

    N = int(N)

    setAs = set(As)

    dictAs: dict[str, int] = dict([(x, 0) for x in setAs])

    results = As.copy()

    for idx, a in enumerate(As):
        count = dictAs.get(a)
        if count != 0:
            results[idx] = results[idx] + "(" + str(count) + ")"

        dictAs[a] += 1

    print("\n".join(results))


if __name__ == "__main__":
    main()
