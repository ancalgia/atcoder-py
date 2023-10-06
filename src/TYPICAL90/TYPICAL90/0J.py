def main(case: str) -> None:
    seito_count, *hoge = case.splitlines()

    scores: list[list[int]] = []

    for x in range(int(seito_count)):
        scores.append(list(map(int, hoge[x].split())))

    sumList1 = []
    sumList2 = []
    tmpSum1 = 0
    tmpSum2 = 0
    for x in scores:
        if x[0] == 1:
            tmpSum1 += x[1]
        else:
            tmpSum2 += x[1]

        sumList1.append(tmpSum1)
        sumList2.append(tmpSum2)

    problems = hoge[int(seito_count) + 1 :]

    for p in problems:
        pass

        a, b = map(int, p.split())

        ans1 = sumList1[b - 1] - (sumList1[a - 2] if a >= 2 else 0)
        ans2 = sumList2[b - 1] - (sumList2[a - 2] if a >= 2 else 0)

        ans = str(ans1) + " " + str(ans2)

        print(ans)


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
        7
        1 72
        2 78
        2 94
        1 23
        2 89
        1 40
        1 75
        1
        2 6
        """,
        """
        7
        1 72
        2 78
        2 94
        1 23
        2 89
        1 40
        1 75
        10
        1 3
        2 4
        3 5
        4 6
        5 7
        1 5
        2 6
        3 7
        1 6
        2 7
        """,
        """
        1
        1 100
        3
        1 1
        1 1
        1 1
        """,
        """
        20
        2 90
        1 67
        2 9
        2 17
        2 85
        2 43
        2 11
        1 32
        2 16
        1 19
        2 65
        1 14
        1 51
        2 94
        1 4
        1 55
        2 90
        1 89
        1 35
        2 81
        20
        3 17
        5 5
        11 11
        8 10
        3 13
        2 6
        3 7
        3 5
        12 18
        4 8
        3 16
        6 8
        3 20
        1 12
        1 6
        5 16
        3 10
        17 19
        4 4
        7 15
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
