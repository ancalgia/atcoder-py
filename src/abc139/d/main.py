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
    N = int(case)

    result = 0

    for x in range(1, N):
        result += x

    print(result)

    # if N == 1:
    #     print(0)
    #     return

    # arr = [x for x in range(1, N + 1)]

    # arr2 = arr[1:] + [arr[0]]

    # result = sum([x[0] % x[1] for x in zip(arr, arr2)])

    # print(result)


if __name__ == "__main__":
    main()
