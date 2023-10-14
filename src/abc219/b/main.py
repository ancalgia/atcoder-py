#!/usr/bin/env python3

import sys

case: str = "".join([x for x in sys.stdin])


def main():
    S1, S2, S3, T = case.split()

    Ss = [S1, S2, S3]

    tmp = ""

    for x in list(T):
        tmp += Ss[int(x) - 1]

    print(tmp)


if __name__ == "__main__":
    main()
