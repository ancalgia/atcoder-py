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
# 3
# 2 -1 -2
#     """
# ).strip()


def main():
    (N,), As = IALL(case)

    current = 0

    result = 0

    step: collections.deque[int] = collections.deque()

    for a in As:
        for x in step:
            current += x
            result = max(result, current)

        current += a

        result = max(result, current)

        if a == 0:
            continue

        elif len(step) == 0:
            step.append(a)

        elif a > 0:
            step.append(step.pop() + a)
            continue

        else:
            if step[-1] < 0:
                step.append(step.pop() + a)
                continue
            else:
                step.append(a)
                continue

    print(result)


if __name__ == "__main__":
    main()
