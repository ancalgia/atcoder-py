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
    S, *_ = SL(case)

    oddS = [x for idx, x in enumerate(S, 1) if idx % 2 == 1]
    evenS = [x for idx, x in enumerate(S, 1) if idx % 2 == 0]

    result: list[str] = []

    for o, e in zip(oddS, evenS):
        result.append(e)
        result.append(o)

    print("".join(result))

    pass


if __name__ == "__main__":
    main()
