#!/usr/bin/env python3

import sys

case: str = "".join([x for x in sys.stdin])


def main():
    (N,), (X, Y), *ABs = [list(map(int, x.split())) for x in case.splitlines()]

    patterns = int(2 ** int(N))

    bestResult = 99999

    for p in range(patterns + 1):
        tmpBit = bin(p)[2:].zfill(N)

        tako = 0
        tai = 0

        # for idx, x in enumerate(ABs):
        #     if idx >= len(tmpBit):
        #         break

        #     if tmpBit[idx] == "1":
        #         tako += x[0]
        #         tai += x[1]

        for idx, b in enumerate(tmpBit):
            if b == "1":
                tako += ABs[idx][0]
                tai += ABs[idx][1]

        if tako >= X and tai >= Y:
            bestResult = min(bestResult, tmpBit.count("1"))

    if bestResult == 99999:
        print(-1)
    else:
        print(bestResult)


if __name__ == "__main__":
    main()
