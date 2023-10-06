import bisect
import itertools
import math

MOD = 1000000007


def mod_m(a: int) -> int:
    return a % MOD


def mod_div(a, b):
    return ((a % MOD) * pow(b, MOD - 2, MOD)) % MOD


def main(case: str) -> None:
    L, R = list(map(int, case.split()))

    # L %= magic_num
    # R %= magic_num

    Lstr = str(L)
    Lcnt = 0

    for x in range(len(Lstr)):
        unit = x + 1

        # Lcnt = m_mod(Lcnt)

        if x != len(Lstr) - 1:
            # 最終行以外は...001~...999

            start = 10**x
            end = 10 ** (x + 1) - 1
            # kaisa = (((start + end) * unit)) * ((end - start + 1) / 2)
            # kaisa = int(m_mod(m_mod((start + end) * unit) * m_mod((end - start + 1) / 2)))
            kaisa = mod_m(mod_m(((start + end) * unit)) * mod_div((end - start + 1), 2))

            Lcnt += kaisa

        else:
            # 最終行はしっかり確認する
            start = 10**x
            end = L - 1
            # kaisa = (((start + end) * unit)) * ((end - start + 1) / 2)
            # kaisa = int(m_mod(m_mod((start + end) * unit) * m_mod((end - start + 1) / 2)))
            kaisa = mod_m(mod_m(((start + end) * unit)) * mod_div((end - start + 1), 2))

            Lcnt += kaisa

    pass

    Rstr = str(R)
    Rcnt = 0

    for x in range(len(Rstr)):
        unit = x + 1

        # Rcnt = m_mod(Rcnt)

        if x != len(Rstr) - 1:
            # 最終行以外は...001~...999

            start = 10**x
            end = 10 ** (x + 1) - 1
            # kaisa = (((start + end) * unit)) * ((end - start + 1) / 2)
            # kaisa = int(m_mod(m_mod((start + end) * unit) * m_mod((end - start + 1) / 2)))
            kaisa = mod_m(mod_m(((start + end) * unit)) * mod_div((end - start + 1), 2))

            Rcnt += kaisa

        else:
            # 最終行はしっかり確認する
            start: int = 10**x
            end = R

            kaisa = mod_m(mod_m(((start + end) * unit)) * mod_div((end - start + 1), 2))
            # kaisa = m_mod((((start + end) * unit)) * ((end - start + 1) / 2))
            # kaisa = int(m_mod(m_mod((start + end) * unit) * m_mod((end - start + 1) / 2)))
            # kaisa = m_mod(m_mod(((start + end) * unit)) * m_mod((end - start + 1) / 2))

            # kaisa = ((m_mod(start + end) * unit)) * (m_mod(end - start + 1) / 2)

            Rcnt += kaisa

    pass

    diff = Rcnt - Lcnt

    print(mod_m(diff))


if __file__.endswith("Main.py"):
    import sys

    case: str = "".join([x for x in sys.stdin])
    main(case)
    exit()

else:
    print("テスト")
    from textwrap import dedent

    test_list: list[str] = [
        #         """
        # 3 5
        #         """,
        #         """
        # 98 100
        #         """,
        #         """
        # 1001 869120
        #         """,
        """
381453331666495446 746254773042091083
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
