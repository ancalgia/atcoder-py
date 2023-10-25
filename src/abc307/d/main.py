#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import re
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def main():
    N, S, *_ = SL(case)

    dq = collections.deque()

    parenCnt = 0

    for x in S:
        if x == "(":
            parenCnt += 1
            dq.append(x)
            continue

        elif x == ")":
            pass
            if parenCnt == 0:
                dq.append(x)
            else:
                while True:
                    pp = dq.pop()
                    if pp == "(":
                        parenCnt -= 1
                        break

        else:
            dq.append(x)

    print("".join(list(dq)))


if __name__ == "__main__":
    main()
