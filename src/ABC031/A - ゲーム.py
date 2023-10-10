import itertools


def main(case: str) -> None:
    AD, *rest = case.splitlines()

    A, D = list(map(int, AD.split()))

    if A >= D:
        D += 1
    else:
        A += 1

    print(A * D)


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
31 87
        """,
        """
101 65
        """,
        """
3 3
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
