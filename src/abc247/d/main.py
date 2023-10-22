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
# 2
# 1 1000000000 1000000000
# 2 1000000000
#     """
# ).strip()


def main():
    (N,), *Qs = IALL(case)

    tutu: collections.deque[list[int]] = collections.deque()

    for q in Qs:
        if q[0] == 1:
            # tgt = [q[1]] * q[2]
            tutu.appendleft([q[1], q[2]])
        else:
            pass

            count = q[1]
            ball = 0
            while count != 0:
                tgt = tutu[-1]
                if tgt[1] >= count:
                    ball += tgt[0] * count

                    tutu[-1][1] -= count
                    break
                else:
                    ball += tgt[0] * tgt[1]
                    count -= tgt[1]
                    tutu.pop()

            print(ball)


if __name__ == "__main__":
    main()
