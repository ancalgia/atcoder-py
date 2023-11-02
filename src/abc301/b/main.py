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

    dq = collections.deque([As[0]])

    current = As[0]

    for x in As[1:]:
        diff = x - current

        if abs(diff) == 1:
            dq.append(x)

        else:
            if diff > 0:
                for z in range(1, abs(diff)):
                    dq.append(current + z)
            else:
                for z in range(1, abs(diff)):
                    dq.append(current - z)

            dq.append(x)

        current = x

    print(*dq)


if __name__ == "__main__":
    main()
