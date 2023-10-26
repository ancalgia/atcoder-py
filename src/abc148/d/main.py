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
    N, As = SL(case)

    N = int(N)

    bricks = list(map(int, As.split()))

    if 1 not in bricks:
        print(-1)
        return

    startidx = 0
    lastidx = 0

    expected_next_brick = 1

    for idx, x in enumerate(bricks):
        if x != expected_next_brick:
            continue

        else:
            if expected_next_brick == 1:
                startidx = idx
                lastidx = idx
            else:
                lastidx = idx

            expected_next_brick += 1

    # print(N - (lastidx - startidx) + expected_next_brick)
    print((startidx) + (N - (lastidx + 1)) + (lastidx - (startidx - 1) - (expected_next_brick - 1)))


if __name__ == "__main__":
    main()
