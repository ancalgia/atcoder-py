def main(case: str) -> None:
    N, *Ss = case.splitlines()

    already_existed_set: set = set()
    already_rejected_set: set = set()

    for idx, x in enumerate(Ss):
        if x in already_rejected_set:
            continue

        if x in already_existed_set:
            already_rejected_set.add(x)
            continue

        already_existed_set.add(x)
        print(idx + 1)


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
5
e869120
atcoder
e869120
square1001
square1001
        """,
        """
4
taro
hanako
yuka
takashi
        """,
        """
10
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
