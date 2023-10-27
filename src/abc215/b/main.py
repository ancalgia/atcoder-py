#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])
# case = "1200000000000000000"
# case = "1152921504606844095"


def main():
    N = int(case)

    # print(math.floor(math.log2(N)))

    tmp = 0
    while True:
        if 2**tmp <= N:
            tmp += 1
            continue
        else:
            print(tmp - 1)
            return


if __name__ == "__main__":
    main()
