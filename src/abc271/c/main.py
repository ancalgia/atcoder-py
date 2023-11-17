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
# 10
# 1 1 1 1 1 1 1 1 1 1
#     """
# ).strip()


def main():
    (N,), As = IALL(case)

    As.sort()

    next = 1

    counter = collections.Counter(As)

    # ダブりを先に数えておく
    sellables = sum([counter[x] - 1 for x in counter])

    bookSet = collections.deque(sorted(set(As)))

    for x in range(10**12):
        if len(bookSet) == 0 and sellables < 2:
            break

        if len(bookSet) > 0 and bookSet[0] == next:
            bookSet.popleft()

            next += 1

        else:
            if len(bookSet) + sellables >= 2:
                if sellables > 0:
                    sellables -= 1
                else:
                    bookSet.pop()

                if sellables > 0:
                    sellables -= 1
                else:
                    bookSet.pop()

                next += 1
                continue
            else:
                break

    print(next - 1)


if __name__ == "__main__":
    main()
