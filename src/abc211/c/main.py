#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import re
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


# 文字列のランレングス圧縮（RLE）
def runLengthEncode(S: str) -> list[tuple[str, int]]:
    grouped = itertools.groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


case: str = "".join([x for x in sys.stdin])


# case = "atcoderrr"


def main():
    S, *_ = SL(case)

    rle = runLengthEncode(S)

    # print(rle)

    result = 0

    S = re.sub(r"[^chokudai]", "", S)

    # rleLen = len(rle)

    dp = [[1, 0, 0, 0, 0, 0, 0, 0, 0] for x in range(len(S) + 1)]

    # dp[0][0] = 1

    for idx, c in enumerate(S, 1):
        for idx2, c2 in enumerate("chokudai", 1):
            if c != c2:
                dp

    # for idx1 in range(rleLen):
    #     if rle[idx1][0] != "c":
    #         continue
    #     for idx2 in range(idx1 + 1, rleLen):
    #         if rle[idx2][0] != "h":
    #             continue
    #         for idx3 in range(idx2 + 1, rleLen):
    #             if rle[idx3][0] != "o":
    #                 continue
    #             for idx4 in range(idx3 + 1, rleLen):
    #                 if rle[idx4][0] != "k":
    #                     continue
    #                 for idx5 in range(idx4 + 1, rleLen):
    #                     if rle[idx5][0] != "u":
    #                         continue
    #                     for idx6 in range(idx5 + 1, rleLen):
    #                         if rle[idx6][0] != "d":
    #                             continue
    #                         for idx7 in range(idx6 + 1, rleLen):
    #                             if rle[idx7][0] != "a":
    #                                 continue
    #                             # result += S[idx7 + 1 :].count("i")

    #                             iCount = sum([x[1] for x in rle[idx7 + 1 :] if x[0] == "i"])

    #                             result += (
    #                                 rle[idx1][1]
    #                                 * rle[idx2][1]
    #                                 * rle[idx3][1]
    #                                 * rle[idx4][1]
    #                                 * rle[idx5][1]
    #                                 * rle[idx6][1]
    #                                 * rle[idx7][1]
    #                                 * iCount
    #                             )
    #                             result %= 10**9 + 7

    # for idx1 in range(len(S)):
    #     if S[idx1] != "c":
    #         continue
    #     for idx2 in range(idx1 + 1, len(S)):
    #         if S[idx2] != "h":
    #             continue
    #         for idx3 in range(idx2 + 1, len(S)):
    #             if S[idx3] != "o":
    #                 continue
    #             for idx4 in range(idx3 + 1, len(S)):
    #                 if S[idx4] != "k":
    #                     continue
    #                 for idx5 in range(idx4 + 1, len(S)):
    #                     if S[idx5] != "u":
    #                         continue
    #                     for idx6 in range(idx5 + 1, len(S)):
    #                         if S[idx6] != "d":
    #                             continue
    #                         for idx7 in range(idx6 + 1, len(S)):
    #                             if S[idx7] != "a":
    #                                 continue
    #                             result += S[idx7 + 1 :].count("i")
    #                             result %= 10**9 + 7

    #                             # for idx8 in range(idx7 + 1, len(S)):
    #                             #     if S[idx8] == "i":
    #                             #         result += 1
    #                             #         result %= 10**9 + 7

    print(result)


if __name__ == "__main__":
    main()
