import itertools


def main(case: str) -> None:
    N = int(case)

    if N % 2 == 1:
        return

    hoge = [["(", ")"]] * N

    selections = set(itertools.product(*([["(", ")"]] * N)))

    half = int(N / 2)

    same_count_selections = ["".join(x) for x in selections if x.count("(") == half]

    for paren in same_count_selections:
        tmp = paren

        while tmp.find("()") != -1:
            if tmp[0] == (")") or tmp[-1] == ("("):
                break

            tmp = tmp.replace("()", "")

        if tmp == "":
            print(paren)


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
2
        """,
        """
3
        """,
        """
4
        """,
        """
10
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
