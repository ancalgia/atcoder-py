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


case: str = "".join([x for x in sys.stdin])


# case = "997764507000"  # ７
# case = "64"  # 3


# case = "1000000000000"  # 8


def main():
    N = int(case)

    if N == 1:
        print(0)
        return

    factors = factorization(N)

    result = 0

    dq: collections.deque[int] = collections.deque()

    resultSet: set[int] = set()

    for x in factors:
        dq.extend([x[0] for _ in range(x[1])])

    tmp = 1

    lastFact = 0

    while True:
        if len(dq) == 0:
            print(len(resultSet))
            return

        if lastFact != dq[0]:
            tmp = 1
            lastFact = dq[0]

        tmp *= dq.popleft()

        if tmp not in resultSet:
            resultSet.add(tmp)
            tmp = 1

    # pass

    # for x in factors:
    #     print(math.log2(x[1]))
    #     result += math.ceil(math.log2(x[1])) or 1

    # print(result)


if __name__ == "__main__":
    main()
