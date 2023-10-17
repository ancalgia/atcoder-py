#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "10"


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

    left = 1
    right = N

    maxResult = 1

    for x in range(N, 0, -1):
        if x == 1:
            print(1)
            return

        hoge = factorization(x)

        if len(hoge) == 1:
            if hoge[0][1] != 1:
                print(x)
                return

        # for piyo in hoge:
        #     if piyo[1] % 2 == 0:
        #         print(x)
        #         return

    # while True:
    #     if left == right:
    #         print(left)
    #         return

    #     tgt = math.ceil((left + right) / 2)

    #     factors = dict([(x[0], x[1]) for x in factorization(tgt)])

    #     if max(factors.values()) >= 2:
    #         maxResult

    #         if left == tgt:
    #             left += 1
    #         else:
    #             left = tgt
    #     else:
    #         if right == tgt:
    #             right -= 1
    #         else:
    #             right = tgt


if __name__ == "__main__":
    main()
