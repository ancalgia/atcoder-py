import itertools


def main(case: str) -> None:
    NL, S = case.splitlines()

    N, L = map(int, NL.split())

    crash_count = 0

    curr_tabs = 1

    for move in S:
        if move == "+":
            curr_tabs += 1
        else:
            curr_tabs -= 1

        if curr_tabs > L:
            crash_count += 1
            curr_tabs = 1

    print(crash_count)


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
6 2
+++-++
        """,
        """
20 20
++-+-+++--+++++-++++
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
