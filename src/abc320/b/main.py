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
    S = case

    for x in range(len(S)):
        tmp_mojisu = len(S) - x

        for pos in range(len(S) - tmp_mojisu + 1):
            tmp_mojiretu = S[pos : pos + tmp_mojisu]
            if tmp_mojiretu == tmp_mojiretu[::-1]:
                print(tmp_mojisu)
                return


if __name__ == "__main__":
    main()
