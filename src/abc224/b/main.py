#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# 3 3
# 2 1 4
# 3 1 3
# 6 4 1

# 2 4
# 4 3 2 1
# 5 6 7 8


def main():
    (H, W), *matrix = IALL(case)

    # 2 1 4
    # 3 1 3
    # 6 4 1

    for h1 in range(H):
        for h2 in range(h1 + 1, H):
            for w1 in range(W):
                for w2 in range(w1 + 1, W):
                    if matrix[h1][w1] + matrix[h2][w2] > matrix[h2][w1] + matrix[h1][w2]:
                        print("No")
                        return

    print("Yes")


if __name__ == "__main__":
    main()
