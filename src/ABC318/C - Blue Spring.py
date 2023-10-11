import itertools
from typing import Literal


def main(case: str) -> None:
    (N, D, P), Fs = [list(map(int, x.split())) for x in case.splitlines()]

    sortedFs = sorted(Fs, reverse=True)

    segmentTotal: list[int] = []

    ticketCount = 0

    for idx, x in enumerate(sortedFs, 1):
        segmentTotal.append(x)

        if idx % D == 0 or idx == len(sortedFs):
            if sum(segmentTotal) >= P:
                ticketCount += 1

                segmentTotal.clear()
            else:
                break

    unuseDays = sortedFs[ticketCount * D :]

    print(ticketCount * P + sum(unuseDays))


if __file__.endswith("Main.py"):
    import sys

    case: str = "".join([x for x in sys.stdin])
    main(case)
    exit()


else:
    print("テスト")
    from textwrap import dedent

    test_list: list[str] = [
        """
5 2 10
7 1 6 3 6
        """,
        """
3 1 10
1 2 3
        """,
        """
8 3 1000000000
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
