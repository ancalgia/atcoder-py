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
    (N,), Ps = IALL(case)

    result: list[tuple[int, int]] = []

    for idx, p in enumerate(Ps, 1):
        result.append((p, idx))

    result.sort()

    resultArr = [str(x[1]) for x in result]

    resultStr = " ".join(resultArr)

    print(resultStr)

    pass


if __name__ == "__main__":
    main()
