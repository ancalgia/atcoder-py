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
# 2 3 2 3 3 3 2 3 3 2
#     """
# ).strip()


def main():
    (N,), As = IALL(case)

    dq: collections.deque[int] = collections.deque()

    lastItemCount = [0, 0]

    curr = 0

    for x in As:
        dq.append(x)

        curr += 1

        if x != lastItemCount[0]:
            lastItemCount = [x, 1]

        else:
            lastItemCount[1] += 1

            if lastItemCount[0] == lastItemCount[1]:
                [dq.pop() for y in range(x)]
                curr -= x

                for idx, z in enumerate(reversed(dq)):
                    if idx == 0:
                        lastItemCount = [z, 1]
                        continue

                    elif z != lastItemCount[0]:
                        break
                    else:
                        lastItemCount[1] += 1

        print(curr)


if __name__ == "__main__":
    main()
