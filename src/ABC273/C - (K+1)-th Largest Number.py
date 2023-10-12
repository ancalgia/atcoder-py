import collections
import itertools


def main(case: str) -> None:
    (N,), As = [list(map(int, x.split())) for x in case.splitlines()]

    revSet = sorted(set(As), reverse=True)

    AsCountDict: dict[int, int] = dict()

    for idx, x in enumerate(revSet):
        AsCountDict[x] = idx

    counts = [AsCountDict[x] for x in As]

    counterDict = dict(collections.Counter(counts))

    pass
    for k in range(N):
        print(counterDict.get(k, 0))


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
6
2 7 1 8 2 8
        """,
        """
1
1
        """,
        """
10
979861204 57882493 979861204 447672230 644706927 710511029 763027379 710511029 447672230 136397527
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("##########テスト入力##########")
        print(test)
        print("   vvvvvvvv出力結果vvvvvvvv")
        main(test)
