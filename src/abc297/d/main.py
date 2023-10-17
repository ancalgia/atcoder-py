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
    A, B = IL(case)

    count = 0

    # left = max(A, B)

    # right = min(A, B)

    while True:
        if A == B:
            print(count)
            return

        if A % B == 0:
            A = A // B
            B = 1

        elif B % A == 0:
            B = B // A
            A = 1

        if A > B:
            if B == 1:
                print(count + A - 1)
                return
            tmp, A = divmod(A, B)

            count += tmp

        else:
            if A == 1:
                print(count + B - 1)
                return
            tmp, B = divmod(B, A)

            count += tmp

        # count += 1


if __name__ == "__main__":
    main()
