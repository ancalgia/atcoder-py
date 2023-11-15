#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = ""


def main():
    X = int(case)

    tmp = 0

    for x in range(1, X + 10):
        tmp += x

        if tmp >= X:
            print(x)
            return

    # minutes: list[set[int]] = []

    # minutes.append(set([0]))

    # for x in range(1, X + 1):
    #     tmpSet: set[int] = set()

    #     for y in minutes[x - 1]:
    #         # minutes[x].update([y - x, y, y + x])
    #         tmpSet.update([y - x, y, y + x])

    #     if X in tmpSet:
    #         print(x)
    #         return

    #     minutes.append(tmpSet)


# for x in range(100):
#     case = x + 1
#     print(case)
#     print("↓↓")
#     main()
#     print("＝＝＝＝")


pass

if __name__ == "__main__":
    main()
