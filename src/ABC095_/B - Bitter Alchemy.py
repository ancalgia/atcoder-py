import itertools


def main(case: str) -> None:
    NX, *rest = case.splitlines()

    N, X = map(int, NX.split())

    donuts = list(map(int, rest))

    make_count = N

    left_zairyo = X - sum(donuts)

    min_donut = min(donuts)

    make_count += left_zairyo // min_donut

    print(make_count)


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
3 1000
120
100
140
        """,
        """
4 360
90
90
90
90
        """,
        """
5 3000
150
130
150
130
110
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
