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
    N, K = IL(case)

    if N == 0:
        print(0)
        return

    if N == 1 or K == 1:
        print(0)
        return

    # ss = set({N})

    naturalSmall1 = N % K
    naturalSmall2 = K % N

    # if N < K:
    #     print(naturalSmall1)
    #     return

    minusSmall1 = naturalSmall1 - K
    minusSmall2 = naturalSmall2 - K

    print(min([abs(naturalSmall1), abs(minusSmall1), abs(naturalSmall2), abs(minusSmall2)]))

    # print(([abs(N // K), abs(K // N)]))

    # while True:
    #     N = abs(N - K)

    #     if N in ss:
    #         print(min(ss))
    #         return

    #     ss.add(N)


if __name__ == "__main__":
    main()
