import itertools


def main(case: str) -> None:
    (N,), As = [list(map(int, x.split())) for x in case.splitlines()]

    kakudos = [0]

    current_kakudo = 0

    for x in As:
        current_kakudo = (current_kakudo + x) % 360

        kakudos.append(current_kakudo)

    kakudos.sort()
    kakudos.append(360)

    print(max([r - l for l, r in zip(kakudos, kakudos[1:])]))


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
4
90 180 45 195
        """,
        """
1
1
        """,
        """
10
215 137 320 339 341 41 44 18 241 149
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
