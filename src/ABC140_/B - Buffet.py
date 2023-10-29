import itertools


def main(case: str) -> None:
    (N,), As, Bs, Cs = [list(map(int, x.split())) for x in case.splitlines()]

    manzoku = 0

    last_food = 99999

    for x in As:
        manzoku += Bs[x - 1]

        if last_food + 1 == x:
            manzoku += Cs[last_food - 1]

        last_food = x

    print(manzoku)


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
3 1 2
2 5 4
3 6
        """,
        """
4
2 3 4 1
13 5 8 24
45 9 15
        """,
        """
2
1 2
50 50
50
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
