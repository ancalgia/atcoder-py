import numpy


def main(case: str) -> None:
    N, K = case.split()

    currnumpy = N

    for _ in range(int(K)):
        currnumpy = numpy.base_repr(int(currnumpy, 8), 9).replace("8", "5", -1)

    # print(curr)
    print(currnumpy)


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
21 1
        """,
        """
1330 1
        """,
        """
2311640221315 15
        """,
        """
77777777777777777777 1
        """,
        """
77777777777777777777 50
        """,
    ]
    # 7611555242456545770
    # 40

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
