#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys
from typing import Literal


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def main():
    (N, Q), *Es = [list(map(int, x.split())) for x in case.splitlines()]

    ppl_stats_list: list[Literal["UNCALLED", "CALLED", "VISITED"]] = ["UNCALLED" for x in range(N)]

    last_called_man = 0

    filteredEs = filter(lambda x: x[0] != 1, Es)

    for x in filteredEs:
        if x[0] == 2:
            ppl_stats_list[x[1] - 1] = "VISITED"
        elif x[0] == 3:
            tgt_idx = ppl_stats_list.index("UNCALLED", last_called_man)

            print(tgt_idx + 1)
            last_called_man = tgt_idx


if __name__ == "__main__":
    main()
