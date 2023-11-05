import itertools


def main(case: str) -> None:
    (N,), Ws, *_ = [list(map(int, x.split())) for x in case.splitlines()]

    ruisekiList: list[int] = []

    summary = 0

    for x in Ws:
        summary += x

        ruisekiList.append(summary)

    smallestAbs = 999999999

    for x in ruisekiList:
        currAbs = abs((ruisekiList[-1] - x) - x)

        if currAbs < smallestAbs:
            smallestAbs = currAbs
        else:
            print(smallestAbs)
            return


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
3
1 2 3
        """,
        """
4
1 3 1 1
        """,
        """
8
27 23 76 2 3 5 62 52
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
