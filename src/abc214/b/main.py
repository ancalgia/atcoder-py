#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "1 0"


def main():
    S, T = IL(case)

    possibles = [x for x in range(0, S + 1)]

    allPtn = list(itertools.product(possibles, possibles, possibles))

    result = 0

    for a, b, c in allPtn:
        if a + b + c <= S and a * b * c <= T:
            result += 1

    print(result)


if __name__ == "__main__":
    main()
