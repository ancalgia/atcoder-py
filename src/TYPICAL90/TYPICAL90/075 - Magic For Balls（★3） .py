import bisect
import itertools
import math

magic_num = 10**9 + 7


# 素因数分解
def factorization(n: int) -> list[list[int]]:
    arr: list[list[int]] = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def main(case: str) -> None:
    N = int(case)

    # hoge = 13
    fuga = factorization(N)
    # piyo = make_divisors(N)

    max_insu = max([x[1] for x in fuga])

    max_log2 = math.log2(max_insu)

    ceiled = math.ceil(max_log2)

    print(len(fuga) - 1 + ceiled)


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
42
        """,
        """
48
        """,
        """
54
        """,
        """
53
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
