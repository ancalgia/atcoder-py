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

# case = "abca"


def main():
    S = case.rstrip()

    counter = collections.Counter(S.replace("(", "").replace("(", ""))

    parenOpenIdx: set[tuple[int, str]] = set([(x.start(), "(") for x in re.finditer(r"\(", S)])

    parenCloseIdx: set[tuple[int, str]] = set([(x.start(), ")") for x in re.finditer(r"\)", S)])

    for c in counter:
        if c == "(" or c == ")":
            continue

        if counter[c] == 1:
            continue

        tgtIdx: set[tuple[int, str]] = set([(x.start(), "X") for x in re.finditer(c, S)])

        checker = sorted((list(tgtIdx) + list(parenOpenIdx) + list(parenCloseIdx)))

        stringified = "".join([x[1] for x in checker])

        while True:
            changed = re.sub(r"\(\)", "", stringified)

            if stringified == changed:
                break

            stringified = changed

        if re.search(r"X[\(]*X", stringified):
            print("No")
            return
        else:
            continue

    # splittedByCloseParen = S.split(")")

    # for c in counter:
    #     if c == "(" or c == ")":
    #         continue
    #     if counter[c] == 1:
    #         continue

    #     for x in splittedByCloseParen:
    #         if x.count(c) >= 2:
    #             print("No")
    #             return

    print("Yes")


if __name__ == "__main__":
    main()
