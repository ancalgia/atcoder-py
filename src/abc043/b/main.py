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
    S, *_ = SL(case)

    dq = collections.deque()

    for c in S:
        if c == "1":
            dq.append("1")

        elif c == "0":
            dq.append("0")
        else:
            if len(dq) != 0:
                dq.pop()

    print("".join(dq))

    pass


if __name__ == "__main__":
    main()
