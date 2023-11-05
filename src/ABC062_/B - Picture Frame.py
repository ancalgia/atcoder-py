import itertools


def main(case: str) -> None:
    HW, *As = case.splitlines()

    H, W = list(map(int, HW.split()))

    print("#" * (W + 2))

    for x in As:
        print(f"#{x}#")

    print("#" * (W + 2))


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
abc
arc
        """,
        """
1 1
z
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
