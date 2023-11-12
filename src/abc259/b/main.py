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
    A, B, D = IL(case)

    # dist = math.sqrt(A**2 + B**2)

    hoge = math.radians(D)

    # 回転後の座標を計算
    x = A * math.cos(hoge) - B * math.sin(hoge)
    y = A * math.sin(hoge) + B * math.cos(hoge)

    # 答えの出力
    print(x, y)

    pass


if __name__ == "__main__":
    main()
