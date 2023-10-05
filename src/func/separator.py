#####　全て数値の二次元配列
def to_all_int_matrix(case: str) -> list[list[int]]:
    return [list(map(int, x.split())) for x in case.splitlines()]


def to_all_int_1_row(case: str) -> list[int]:
    return list(map(int, case.split()))


def slide_diff_list(tgtlist: list):
    return [r - l for l, r in zip(tgtlist, tgtlist[1:])]


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


# 約数の列挙
def make_divisors(n: int) -> list[int]:
    lower_divisors: list[int] = []
    upper_divisors: list[int] = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
