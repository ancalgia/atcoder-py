#!/usr/bin/env python3

import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys

import decimal  # isort: skip


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def main():
    N = math.floor(float(case.strip()))

    # print(int(case.strip()[-3]))

    if int(case.strip()[-3]) >= 5:
        N += 1

    print(N)


if __name__ == "__main__":
    main()
