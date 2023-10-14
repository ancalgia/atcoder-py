#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


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


def main():
    N = int(case)

    tmpN = N
    tmpDiv2 = 0

    for x in range(5000):
        if tmpN % 2 == 0:
            tmpDiv2 += 1
            tmpN //= 2

        else:
            break

    tmpDiv3 = 0

    for x in range(5000):
        if tmpN % 3 == 0:
            tmpDiv3 += 1
            tmpN //= 3

        else:
            break

    if tmpN == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
