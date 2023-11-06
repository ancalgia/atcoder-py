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
    (N, D), *Xs = IALL(case)

    result = 0

    for x in range(N):
        for y in range(x + 1, N):
            tmp = math.sqrt(sum([(a - b) ** 2 for a, b in zip(Xs[x], Xs[y])]))

            f, i = math.modf(tmp)

            if f == 0:
                result += 1

    print(result)


if __name__ == "__main__":
    main()
