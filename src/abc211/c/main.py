#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import re
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def main():
    S, *_ = SL(case)

    result = 0

    S = re.sub(r"[^chokudai]", "", S)

    for idx1 in range(len(S)):
        if S[idx1] != "c":
            continue
        for idx2 in range(idx1 + 1, len(S)):
            if S[idx2] != "h":
                continue
            for idx3 in range(idx2 + 1, len(S)):
                if S[idx3] != "o":
                    continue
                for idx4 in range(idx3 + 1, len(S)):
                    if S[idx4] != "k":
                        continue
                    for idx5 in range(idx4 + 1, len(S)):
                        if S[idx5] != "u":
                            continue
                        for idx6 in range(idx5 + 1, len(S)):
                            if S[idx6] != "d":
                                continue
                            for idx7 in range(idx6 + 1, len(S)):
                                if S[idx7] != "a":
                                    continue
                                for idx8 in range(idx7 + 1, len(S)):
                                    if S[idx8] == "i":
                                        result += 1
                                        result %= 10**9 + 7

    print(result)


if __name__ == "__main__":
    main()
