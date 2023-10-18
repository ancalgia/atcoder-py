#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "1000000000000"


def main():
    H = int(case)

    if H == 1:
        print(1)
        return

    # rt = math.sqrt(H).__floor__()
    rt = math.log2(H).__floor__()

    print((2 ** (rt + 1)) - 1)
    pass


if __name__ == "__main__":
    main()
