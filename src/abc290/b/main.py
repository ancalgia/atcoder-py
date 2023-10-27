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
    NK, S = SL(case)

    N, K = IL(NK)

    result = ""

    passed = 0

    for s in S:
        if s == "o" and passed < K:
            result += "o"
            passed += 1
            continue
        else:
            result += "x"

    print(result)

    pass


if __name__ == "__main__":
    main()
