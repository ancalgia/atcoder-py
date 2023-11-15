#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])
# case = "10 7 96"

# case = "1234 56789 314159265"


# case = "1000000000 1000000000 100"


# case = "2 1 100000000000"


def main():
    A, B, X = IL(case)

    minSeisu = 1

    if A * 1 + B * 1 > X:
        print(0)
        return

    maxSeisu = 10**9

    if A * maxSeisu + B * len(str(maxSeisu)) <= X:
        print(maxSeisu)
        return

    while True:
        if minSeisu == maxSeisu:
            print(minSeisu)
            return

        tgt = (minSeisu + maxSeisu) // 2

        if tgt == minSeisu:
            print(tgt)
            return

        tgtPrice = A * tgt + B * len(str(tgt))

        if tgt == minSeisu:
            if tgtPrice <= X:
                print(minSeisu)
                return
            else:
                print(minSeisu + 1)
                return

        if tgt == maxSeisu:
            if tgtPrice <= X:
                print(maxSeisu)
                return
            else:
                print(minSeisu)
                return

        if tgtPrice <= X:
            if maxSeisu - minSeisu == 1:
                minSeisu += 1
            else:
                minSeisu = tgt

        else:
            if maxSeisu - minSeisu == 1:
                minSeisu -= 1
            else:
                maxSeisu = tgt


if __name__ == "__main__":
    main()
