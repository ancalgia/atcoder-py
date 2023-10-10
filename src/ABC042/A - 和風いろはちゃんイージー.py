import itertools


def main(case: str) -> None:
    ABC, *_ = case.splitlines()

    A, B, C = sorted(ABC.split())

    if A == "5" and B == "5" and C == "7":
        print("YES")
    else:
        print("NO")


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
5 5 7
        """,
        """
7 7 5
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
