import bisect
import itertools
import math

MOD = 1000000007


def mod_m(a: int) -> int:
    return a % MOD


def mod_div(a, b):
    return ((a % MOD) * pow(b, MOD - 2, MOD)) % MOD


def main(case: str) -> None:
    N, *SCs = [list(map(int, x.split())) for x in case.splitlines()]

    scDicts = dict([(str(x[0]), x[1]) for x in SCs])

    pass

    while True:
        # for x in range(len(scDicts)):
        isExit = True

        for x in scDicts:
            if scDicts[x] >= 2:
                isExit = False
                # half = math.floor(scDicts[x] / 2)
                half = math.floor(math.sqrt(scDicts[x]))

                scDicts[x] %= 2

                if scDicts.get(str(int(x) * half)):
                    scDicts[str(int(x) * half)] += 1
                else:
                    scDicts[str(int(x) * half)] = 1

                break

        if isExit:
            print(len([x for x in scDicts if scDicts[x] != 0]))

            return


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
3 3
5 1
6 1
        """,
        """
3
1 1
2 1
3 1
        """,
        """
1
1000000000 1000000000
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
