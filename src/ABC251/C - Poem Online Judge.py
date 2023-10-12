# import bisect


def main(case: str) -> None:
    N, *Ss = case.splitlines()

    poemAndScores = [x.split() for x in Ss]

    poemSet = set([x[0] for x in poemAndScores])

    maxScore = 0

    maxIdx = 99999999

    for idx, x in enumerate(poemAndScores):
        if x[0] in poemSet:
            poemSet.remove(x[0])

            if maxScore < int(x[1]):
                maxScore = int(x[1])
                maxIdx = idx

    print(maxIdx + 1)


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
aaa 10
bbb 20
aaa 30
        """,
        """
5
aaa 9
bbb 10
ccc 10
ddd 10
bbb 11
        """,
        """
10
bb 3
ba 1
aa 4
bb 1
ba 5
aa 9
aa 2
ab 6
bb 5
ab 3
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
