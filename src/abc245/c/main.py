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
    (N, K), As, Bs = [list(map(int, x.split())) for x in case.splitlines()]

    # 次で使っていい値（0＝両方）
    enable_next_start = [True, True]

    for x in range(N - 1):
        if enable_next_start == [True, True]:
            result = [
                abs(As[x] - As[x + 1]) <= K or abs(Bs[x] - As[x + 1]) <= K,
                abs(As[x] - Bs[x + 1]) <= K or abs(Bs[x] - Bs[x + 1]) <= K,
            ]
        elif enable_next_start == [True, False]:
            result = [
                abs(As[x] - As[x + 1]) <= K,
                abs(As[x] - Bs[x + 1]) <= K,
            ]
        else:
            pass
            result = [
                abs(Bs[x] - As[x + 1]) <= K,
                abs(Bs[x] - Bs[x + 1]) <= K,
            ]

        if any(result):
            enable_next_start = result
        else:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
