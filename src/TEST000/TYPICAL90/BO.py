def base10int(value: int, base: int) -> str:
    if int(value / base):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)


def main(case: str) -> None:
    N, K = case.split()

    curr = N

    for _ in range(int(K)):
        curr = base10int(int(int(curr, 8)), 9).replace("8", "5")

    print(curr)


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
21 1
        """,
        """
1330 1
        """,
        """
2311640221315 15
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
