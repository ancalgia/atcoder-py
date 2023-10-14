#!/usr/bin/env python3

import sys

case: str = "".join([x for x in sys.stdin])


def main():
    if len(set(list(case))) != len(case):
        print("No")
        return

    if case != "".join(list(sorted(case, reverse=True))):
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
