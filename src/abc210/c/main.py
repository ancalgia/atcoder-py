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
# 7 6
# 1 2 2 2 3 3 4
#     """
# ).strip()


def main():
    (N, K), Cs = IALL(case)

    if N == K:
        print(len(set(Cs)))
        return

    maxResult = 0

    # dq = collections.deque()
    counter = collections.Counter()

    isFirst = True

    for x in range(N - K + 1):
        if isFirst:
            tgt = Cs[:K]

            # dq.extend(tgt)

            counter.update(tgt)
            isFirst = False

        else:
            popped = Cs[x - 1]

            if counter[popped] == 1:
                counter.pop(popped)
            else:
                counter[popped] -= 1

            # dq.append(Cs[K + x])

            counter[Cs[K + x - 1]] += 1

        maxResult = max([maxResult, len(counter)])

    print(maxResult)


if __name__ == "__main__":
    main()
