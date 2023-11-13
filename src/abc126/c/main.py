#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "3 10"


def main():
    N, K = IL(case)

    results = []

    for x in range(1, N + 1):
        if x >= K:
            results.append(1)
            # print(1)
            continue

        else:
            coin = math.ceil(math.log2(K / x))

            results.append(1 / 2**coin)

    print(sum(results) / len(results))

    pass


if __name__ == "__main__":
    main()
