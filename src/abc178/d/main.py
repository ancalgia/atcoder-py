#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "7"


def main():
    N = int(case)

    if N < 3:
        print(0)
        return

    ketaMax = N // 3

    result = 0

    for x in range(1, ketaMax + 1):
        if x == 1:
            result += 1
            continue

        hasu = N - (3 * x)

        if hasu == 0:
            result += 1
            continue

        # 重複組み合わせの数
        tmp = math.comb((hasu + 1) + (x - 1) - 1, x - 1)
        result += tmp

        result %= 10**9 + 7

    print(result)


if __name__ == "__main__":
    main()
