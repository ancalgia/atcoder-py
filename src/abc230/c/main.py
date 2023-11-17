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
    (N, A, B), (P, Q, R, S) = IALL(case)

    result: list[str] = []

    for x in range(P, Q + 1):
        tmp: list[str] = []

        for y in range(R, S + 1):
            if abs(x - A) == abs(y - B):
                tmp.append("#")
            else:
                tmp.append(".")

        result.append("".join(tmp))

    [print(x) for x in result]


if __name__ == "__main__":
    main()
