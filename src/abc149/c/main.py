#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def isPrime(n):
    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n == 1:
        return False

    return True


def main():
    N = int(case)

    while True:
        if isPrime(N):
            print(N)
            return
        N += 1


if __name__ == "__main__":
    main()
