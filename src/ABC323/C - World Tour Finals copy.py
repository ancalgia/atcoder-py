import bisect
import itertools
import math

MOD = 1000000007


def mod_m(a: int) -> int:
    return a % MOD


def mod_div(a, b):
    return ((a % MOD) * pow(b, MOD - 2, MOD)) % MOD


def main(case: str) -> None:
    NM, As, *Ss = case.splitlines()

    N, M = map(int, NM.split())

    AList = list(map(int, As.split()))


    for x in Ss:
        



    total = 0
    for x in Alist:
        total += mod_m(x * (Asum - x))

    print(mod_div(mod_m(total), 2))


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
3 4
1000 500 700 2000
xxxo
ooxx
oxox
        """,
        """
5 5
1000 1500 2000 2000 2500
xxxxx
oxxxx
xxxxx
oxxxx
oxxxx
        """,
        """
7 8
500 500 500 500 500 500 500 500
xxxxxxxx
oxxxxxxx
ooxxxxxx
oooxxxxx
ooooxxxx
oooooxxx
ooooooxx
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
