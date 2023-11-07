#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "abaababaab"


def main():
    S, *_ = SL(case)

    result = 2
    S = S[:-2]

    while True:
        length = len(S) // 2

        if S[:length] == S[length:]:
            print(len(S))
            return

        result += 2
        S = S[:-2]


if __name__ == "__main__":
    main()
