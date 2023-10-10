# import bisect


def main(case: str) -> None:
    N, *Ss = case.splitlines()

    win_idx_list = []

    for idx, x in enumerate(Ss):
        curr = [0, 0]

        curr[0] = x.count("o")
        curr[1] = idx + 1

        win_idx_list.append(curr.copy())

    sorted_list = sorted(win_idx_list, key=lambda x: (-(x[0]), x[1]))

    # print(sorted_list)
    [print(x[1]) for x in sorted_list]


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
-xx
o-x
oo-
        """,
        """
7
-oxoxox
x-xxxox
oo-xoox
xoo-ooo
ooxx-ox
xxxxx-x
oooxoo-
        """,
        #         """
        # 10000 1 1
        #         """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
