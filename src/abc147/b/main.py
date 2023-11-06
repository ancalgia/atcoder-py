#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "abcdefg"


def main():
    S, *_ = SL(case)

    frontS = S[: len(S) // 2]
    backS = S[::-1][: len(S) // 2]

    result = 0

    for a, b in zip(frontS, backS):
        if a != b:
            result += 1

    print(result)


if __name__ == "__main__":
    main()
