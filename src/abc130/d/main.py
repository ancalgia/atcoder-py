#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# from textwrap import dedent

# case = dedent(
#     """
# 4 10
# 6 1 2 7
#     """
# ).strip()


def main():
    (N, K), As = IALL(case)

    left = 0
    right = 0

    curr_size = 0

    result = 0

    # 尺取り法
    while True:
        if curr_size < K:
            if right >= len(As):
                break

            curr_size += As[right]
            right += 1
        else:
            result += N - right + 1

            curr_size -= As[left]
            left += 1

    print(result)


if __name__ == "__main__":
    main()
