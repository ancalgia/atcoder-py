import bisect
import itertools
import math


def main(case: str) -> None:
    (NK, *As) = [list(map(int, x.split())) for x in case.splitlines()]

    N, K = NK

    # 獲得する得点の配列（完答時は完答点-部分点）
    hoge = [[x[0] - x[1], x[1]] for x in As]

    # 展開して高い順に並べ替え(完答点が部分点より高くなることはないため、素朴に並べ替えてよいもよう)
    gettable_scores = sorted(itertools.chain.from_iterable(hoge), reverse=True)

    print(sum(gettable_scores[:K]))


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
4 3
4 3
9 5
15 8
8 6
        """,
        """
2 2
7 6
3 2
        """,
        """
10 12
987753612 748826789
36950727 36005047
961239509 808587458
905633062 623962559
940964276 685396947
959540552 928301562
60467784 37828572
953685176 482123245
87983282 66762644
912605260 709048491
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
