import itertools


def main(case: str) -> None:
    S, *_ = case.splitlines()

    doubleS = S + S

    strings: list[str] = []

    for x in range(len(S)):
        strings.append(doubleS[x : x + len(S)])

    # strSet = set(strings)

    strings.sort()

    first = strings[0]
    last = strings[-1]

    print(first)
    print(last)


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
aaba
        """,
        """
z
        """,
        """
abracadabra
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
