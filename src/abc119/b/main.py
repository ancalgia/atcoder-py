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
    N, *XUs = SL(case)

    JPYs = 0
    BTCs = 0
    for xu in XUs:
        x, u = xu.split()

        if u == "JPY":
            JPYs += int(x)

        else:
            BTCs += float(x)

    print(JPYs + BTCs * 380000)


if __name__ == "__main__":
    main()
