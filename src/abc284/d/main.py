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
# 63
# 8469564796182716693
# 7761701608577533717
# 7785474889392445051
# 7738011461615384203
# 3870530781010357421
# 4906678917709732283
# 6814139676657033349
# 4219818992637875743
# 3415080039783565427
#     """
# ).strip()


def main():
    (N,), *Ts = IALL(case)

    N = int(N)

    Ts = [x[0] for x in Ts]

    for t in Ts:
        tmp = 2
        while True:
            if t % tmp != 0:
                tmp += 1
                continue

            f, s = math.modf(math.sqrt(t // tmp))

            if f == 0:
                print(int(s), tmp)
            else:
                print(tmp, (t // tmp) // tmp)

            break


if __name__ == "__main__":
    main()
