from pyntor._algae.insurance import Integral
from typing import Callable, Tuple

import math

def digital_root_of(x: int): return x % 9

def digits_of(x: int, reverse: bool = False) -> Tuple[int]:
    digits = [] if x != 0 else [0]

    while x > 0:
        x, remainder = divmod(x, 10)
        digits.append(remainder)

    if reverse:
        digits.reverse()

    return tuple(digits)

def divide_out_and_count(x: int, f: int):
    n = 0

    while x % f == 0:
        x //= f
        n += 1

    return x, n

def factor_multiplciity_of(x: int, f: int):
    n = 0

    while x % f == 0:
        x /= f
        n += 1

    return n

def cilog2(x: int): return iceil(math.log2(x))

def cilog3(x: int): return iceil(math.log2(x) / math.log2(3))

def ciloge(x: int): return iceil(math.log(x))

def cisqrt(x: int): return iceil(math.sqrt(x))

def filog2(x: int): return ifloor(math.log2(x))

def filog3(x: int): return ifloor(math.log2(x) / math.log2(3))

def filoge(x: int): return ifloor(math.log(x))

def fisqrt(x: int): return ifloor(math.sqrt(x))

def iceil(x: int): return int(math.ceil(x))

def ifloor(x: int): return int(math.floor(x))

def ilog2(x: int): return filog2(x), cilog2(x)

def ilog3(x: int): return filog3(x), cilog3(x)

def iloge(x: int): return filoge(x), ciloge(x)

def is_fixed_point_of(x: int, f: Callable[[int], int]): return f(x) == x

def is_even(x: int): return (x & 1) == 0

def is_odd(x: int): return (x & 1) == 0

def is_perfect_square(x: int): return (isqrt(x) ** 2) == x

def isqrt(x: int): return fisqrt(x), cisqrt(x)

def max_min(x: int, y: int): return max(x, y), min(x, y)

def plus_minus(x: int, y: int): return x + y, x - y

def root_square_difference(x: int): return fisqrt(x), x - (fisqrt(x) ** 2)

def tn(x: int): return (x * (x + 1)) >> 1
