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
    N, S, M, L = IL(case)

    minPrice = 10**20

    for roku in range(100):
        if roku * 6 >= N:
            minPrice = min(minPrice, S * roku)
            break

        for hati in range(100):
            if (roku * 6) + (hati * 8) >= N:
                minPrice = min(minPrice, (S * roku) + (M * hati))
                break

            for ele in range(100):
                if (roku * 6) + (hati * 8) + (ele * 12) >= N:
                    minPrice = min(minPrice, (S * roku) + (M * hati) + (L * ele))
                    break

    print(minPrice)


if __name__ == "__main__":
    main()
