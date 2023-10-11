import itertools
from typing import Literal


def format_a(a: list[int]) -> list[int]:
    if a[0] == 1:
        return [a[1] * 2, a[2] * 2]
    if a[0] == 2:
        return [a[1] * 2, a[2] * 2 - 1]
    if a[0] == 3:
        return [a[1] * 2 + 1, a[2] * 2]
    if a[0] == 4:
        return [a[1] * 2 + 1, a[2] * 2 - 1]

    raise Exception


def main(case: str) -> None:
    (N,), *As = [list(map(int, x.split())) for x in case.splitlines()]

    formattedAs = [format_a(x) for x in As]

    count = 0

    for x_idx in range(N):
        for y_idx in range(x_idx + 1, N):
            if formattedAs[x_idx][0] <= formattedAs[y_idx][1] and formattedAs[x_idx][1] >= formattedAs[y_idx][0]:
                count += 1

    print(count)


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
1 1 2
2 2 3
3 2 4
        """,
        """
19
4 210068409 221208102
4 16698200 910945203
4 76268400 259148323
4 370943597 566244098
1 428897569 509621647
4 250946752 823720939
1 642505376 868415584
2 619091266 868230936
2 306543999 654038915
4 486033777 715789416
1 527225177 583184546
2 885292456 900938599
3 264004185 486613484
2 345310564 818091848
1 152544274 521564293
4 13819154 555218434
3 507364086 545932412
4 797872271 935850549
2 415488246 685203817
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
