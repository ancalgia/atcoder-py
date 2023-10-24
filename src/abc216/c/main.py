#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "8000000000000000000"


def main():
    N = int(case)

    result = N

    # isEven = N%2==0

    lastStr = ""

    while True:
        if result == 0:
            print(lastStr)
            return

        if result % 2 != 0:
            # 奇数なら末尾を外へ
            result = result - 1
            lastStr = "A" + lastStr

        else:
            # 偶数なら文字を半分にしてBを付与
            result = result // 2
            lastStr = "B" + lastStr


if __name__ == "__main__":
    main()
