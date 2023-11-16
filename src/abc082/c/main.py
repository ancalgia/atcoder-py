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
    (N,), As = IALL(case)

    AsCounter = collections.Counter(As)

    result = 0

    for x in AsCounter:
        count = AsCounter[x]

        if x == count:
            # いい数
            continue

        elif x < count:
            # 多いから減らす
            result += count - x

        else:
            # 少ないから全部消す
            result += count

    print(result)


if __name__ == "__main__":
    main()
