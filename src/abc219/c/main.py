#!/usr/bin/env python3

import sys

case: str = "".join([x for x in sys.stdin])


def main():
    X, N, *Ss = case.splitlines()

    encoder = str.maketrans(X, "abcdefghijklmnopqrstuvwxyz")
    decoder = str.maketrans("abcdefghijklmnopqrstuvwxyz", X)

    for x in range(len(Ss)):
        Ss[x] = Ss[x].translate(encoder)

    Ss.sort()

    for x in range(len(Ss)):
        Ss[x] = Ss[x].translate(decoder)
        print(Ss[x])


if __name__ == "__main__":
    main()
