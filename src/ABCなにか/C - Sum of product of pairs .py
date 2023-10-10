import bisect
import itertools
import math

MOD = 1000000007


def mod_m(a: int) -> int:
    return a % MOD

def mod_div(a, b):
    return ((a % MOD) * pow(b, MOD - 2, MOD)) % MOD


def main(case: str) -> None:
    N, As = case.splitlines()

    Alist = list(map(int, As.split()))

    Asum = sum(Alist)

    total = 0
    for x in Alist:
        total +=mod_m( x *(Asum - x))
        

    print(mod_div(mod_m(total),2))

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
1 2 3 
        """,
        """
4
141421356 17320508 22360679 244949
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
