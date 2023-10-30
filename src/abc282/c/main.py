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
# 20
# a,"t,"c,"o,"d,"e,"r,
#     """
# ).strip()


def main():
    N, S = SL(case)

    dq = collections.deque()

    inDoubleQuote = False

    for x in S:
        if not inDoubleQuote and x == ",":
            dq.append(".")
        elif x == '"':
            dq.append(x)
            inDoubleQuote = not inDoubleQuote

        else:
            dq.append(x)

    print("".join(dq))


if __name__ == "__main__":
    main()
