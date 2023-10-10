# import bisect


def main(case: str) -> None:
    S = case

    arr = [x for idx, x in enumerate(S) if idx % 2 == 1 and x != "0"]

    if len(arr) == 0:
        print("Yes")
    else:
        print("No")


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
1000 15 80
        """,
        """
2000 20 100
        """,
        """
10000 1 1
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
