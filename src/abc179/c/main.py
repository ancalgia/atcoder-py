#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


# 素因数分解
def factorization(n: int) -> list[list[int]]:
    arr: list[list[int]] = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


# case: str = "".join([x for x in sys.stdin])

case = "100"


def main():
    N = int(case)

    result = 0

    for x in range(1, N + 1):
        ab = N - x

        hoge = factorization(ab)

        pass

    pass


if __name__ == "__main__":
    main()
