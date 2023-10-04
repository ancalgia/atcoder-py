#####　全て数値の二次元配列
def to_all_int_matrix(case: str) -> list[list[int]]:
    return [list(map(int, x.split())) for x in case.splitlines()]


def to_all_int_1_row(case: str) -> list[int]:
    return list(map(int, case.split()))
