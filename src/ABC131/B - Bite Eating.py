import itertools


def main(case: str) -> None:
    NL, *_ = case.splitlines()

    N, L = list(map(int, NL.split()))

    tasteSet = set([x + L - 1 for x in range(1, N + 1)])

    result = min(tasteSet, key=abs)

    tasteSet.remove(result)

    print(sum(tasteSet))


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
5 2
        """,
        """
3 -1
        """,
        """
30 -50
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
