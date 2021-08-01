from typing import List


def pencils_of_rays(m: int, n: int) -> int:
    return count_odd_numbers(xs=list_of_floors(m=m, n=n))


def floor_division_squares(x: int, y: int) -> int:
    return (y*y) // (x*x)


def is_odd(x: int) -> bool:
    return not x % 2 == 0


def count_odd_numbers(xs: List[int]) -> int:
    return len([x for x in xs if is_odd(x)])


def list_of_floors(m: int, n: int) -> List[int]:
    _m: int = m+1
    _n: int = n+1
    return [floor_division_squares(x=x, y=y)
            for x in range(_m, _n) for y in range(_m, _n)]
