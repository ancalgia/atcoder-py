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
    ABCDE = IL(case)

    ABCDE.sort(key=lambda x: int(str(x - 1)[-1]), reverse=True)

    result = sum([math.ceil(x / 10) * 10 for x in ABCDE[:-1]]) + ABCDE[-1]

    print(result)


if __name__ == "__main__":
    main()
