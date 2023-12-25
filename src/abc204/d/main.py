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
# 18
# 959 822 127 677 905 486 152 785 659 577 263 114 261 286 837 680 737 352
#     """
# ).strip()  # 4840


def main():
    (N,), Ts = IALL(case)

    if N == 1:
        print(Ts[0])
        return

    Ts.sort(reverse=True)

    alltime = sum(Ts)

    dp: set[int] = set([0])

    for t in Ts:
        tmpSet: set[int] = set()
        for x in dp:
            tmpSet.add(x + t)

        dp.update(tmpSet)

    sortedDp = sorted(list(dp))

    tgtidx = bisect.bisect_left(sortedDp, alltime / 2)

    maybe1 = max(sortedDp[tgtidx], alltime - sortedDp[tgtidx])
    maybe2 = max(sortedDp[tgtidx + 1], alltime - sortedDp[tgtidx + 1])

    print(min(maybe1, maybe2))

    # for t in Ts:
    #     if oven1 <= oven2:
    #         oven1 += t
    #     else:
    #         oven2 += t

    # print(max(oven1, oven2))


if __name__ == "__main__":
    main()
