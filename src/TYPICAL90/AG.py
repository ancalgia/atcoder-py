import math


def main(case: str) -> None:
    H, W = map(int, case.split())

    a = math.ceil(H / 2) * math.ceil(W / 2)

    print(a if H != 1 and W != 1 else H * W)


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
2 3
        """,
        """
3 4
        """,
        """
3 6
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
