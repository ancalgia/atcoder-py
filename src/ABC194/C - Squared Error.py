import itertools


def main(case: str) -> None:
    (N,), As = [list(map(int, x.split())) for x in case.splitlines()]

    # allComb = itertools.combinations(As, 2)

    # allDiffs = [abs(x[0] - x[1]) for x in allComb]

    allDiffs = [abs(x[0] - x[1]) for x in itertools.combinations(As, 2)]

    allDiffsComb = itertools.combinations(allDiffs, 2)

    # allDiffMultis = [(x[0] * x[1]) for x in allDiffsComb]

    # print((sum(allDiffs) ** 2) - (sum(allDiffMultis) * 2))

    allDiffMultis = sum([(x[0] * x[1]) for x in allDiffsComb])

    print((sum(allDiffs) ** 2) - (allDiffMultis * 2))


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
2 8 4
        """,
        """
5
-5 8 9 -4 -3
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("##########テスト入力##########")
        print(test)
        print("   vvvvvvvv出力結果vvvvvvvv")
        main(test)
