def main(case: str) -> None:
    S = case

    for x in range(len(S)):
        tmp_mojisu = len(S) - x

        for pos in range(len(S) - tmp_mojisu + 1):
            tmp_mojiretu = S[pos : pos + tmp_mojisu]
            if tmp_mojiretu == tmp_mojiretu[::-1]:
                print(tmp_mojisu)
                return


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
TOYOTA
        """,
        """
ABCDEFG
        """,
        """
AAAAAAAAAA
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
