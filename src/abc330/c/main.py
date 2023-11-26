#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


# 約数の列挙
def make_divisors(n: int) -> list[int]:
    lower_divisors: list[int] = []
    upper_divisors: list[int] = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


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


case: str = "".join([x for x in sys.stdin])

# case = ""


def main():
    D = int(case)

    keys: list[int] = []

    for x in range(D + 20):
        tmp = x**2
        keys.append(tmp)

        if tmp >= (D + 20) * 10:
            break

    minDiff = D * 100

    # dp = [keys.copy()]

    for x in keys:
        tgt = D - x

        tgtIdx = bisect.bisect(keys, tgt)

        minDiff = min(
            minDiff,
            abs(tgt - keys[tgtIdx]),
            abs(tgt - keys[tgtIdx - (1 if tgtIdx != 0 else 0)]),
        )

    # minX =

    # for x in keys:
    #     for y in keys:
    #         tmp = abs(x + y - D)
    #         if minDiff > tmp:
    #             minDiff = tmp

    #         if (x + y - D) > 10:
    #             break

    # allSet = itertools.combinations_with_replacement(keys, 2)

    # # print(len(allSet))

    # hogege = min([abs(x[0] + x[1] - D) for x in allSet])

    # print(hogege)

    # hoge = make_divisors(D)
    # piyo = factorization(D)
    print(minDiff)
    pass


if __name__ == "__main__":
    main()
