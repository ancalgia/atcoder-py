def main(case: str) -> None:
    x, *y = case.splitlines()
    pass

    y.reverse()

    for hoge in y:
        print(hoge)

    # if (x * y) % 2 == 0:
    #     print("Even")
    # else:
    #     print("Odd")


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
        Takahashi
        Aoki
        Snuke
        """,
        """
        4
        2023
        Year
        New
        Happy
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
