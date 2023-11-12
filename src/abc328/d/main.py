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

    for x in S:
        if x == "C" and len(dq) >= 2:
            last1 = dq.pop()
            last2 = dq.pop()

            if last2 == "A" and last1 == "B":
                continue
            else:
                dq.extend([last2, last1, x])
                continue

        dq.append(x)

    print("".join(dq))

    pass


if __name__ == "__main__":
    main()
