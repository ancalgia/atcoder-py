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
    N, *Ss = SL(case)

    pass

    # 1 文字目は H , D , C , S のどれかである。
    # 2 文字目は A , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , T , J , Q , K のどれかである。

    SsSet = set(Ss)

    if len(Ss) != len(SsSet):
        print("No")
        return

    for x in Ss:
        if x[0] not in ["H", "D", "C", "S"]:
            print("No")
            return
        if x[1] not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
