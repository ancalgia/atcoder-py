#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# N K X
# 5 4 7
# 8 3 10 5 13
# 出力例 1
# Copy
# 12


def main():
    (N, K, X), As = IALL(case)

    over7Count = 0

    modAs: list[int] = []

    for a in As:
        d, m = divmod(a, X)

        over7Count += d
        modAs.append(m)

    modAs.sort(reverse=True)

    if K <= over7Count:
        print((over7Count - K) * X + sum(modAs))
        return

    else:
        leftCoupon = K - over7Count

        if leftCoupon >= len(modAs):
            print(0)
            return
        else:
            print(sum(modAs[leftCoupon:]))
            return


if __name__ == "__main__":
    main()
