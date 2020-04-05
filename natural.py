from pyntor._algae.decorators import raise_instead
from pyntor._algae.insurance import Integral
from pyntor._algae.math import digits_of
from secrets import randbelow
from typing import Callable, Final,  Iterable, Tuple, Union

__all__ = ['Natural', 'NaturalType']

class Natural(int):

    RAND_MAX: Final[int] = 2147483648

    def __new__(cls, value: Union[int, str, Iterable]):
        if isinstance(value, Iterable):
            value = int(''.join(map(str, value)))
        else:
            value = int(value)

        return int.__new__(cls, Integral.ensure_in_natural(value))

    def __init__(self, value: Union[int, str, Iterable] = 0):

        self.__digits = digits_of(int(self))
        self.__convert_digits = True

        self.__digit_sum = None
        self.__length = len(self.__digits)

    @classmethod
    def random(cls, max_value: int = 100): return cls(randbelow(Natural(max_value)))

    @staticmethod
    def naturalize(values: Iterable): return [Natural(value) for value in values]

    @staticmethod
    def naturals(start: int, end: Union[int, None] = None, step: int = 1):

        if end is None:
            return [Natural(i) for i in range(0, start, step)]
        else:
            reverse = start > end

            if reverse:
                start, end = (end + 1), (start + 1)

            values = [Natural(i) for i in range(start, end, step)]

            return values[::-1] if reverse else values

    @staticmethod
    def random_sequence(length, max_value: int = 100): [Natural(rand_below(max_value)) for _ in range(length)]

    @staticmethod
    def repeat(value: int, count: int): return [Natural(value)] * count

    @property
    def digits(self) -> Tuple:
        if self.__convert_digits:
            self.__digits = tuple([Natural(digit) for digit in self.__digits]) if len(self.__digits) > 1 else [self]
            self.__convert_digits = False

        return self.__digits

    def count(self, digit: int) -> int: return self.__digits.count(digit)

    def __add__(self, x: int):
        result = super().__add__(x)
        return result if not (isinstance(result, int) and result >= 0) else Natural(result)

    def __sub__(self, x: int):
        result = super().__sub__(x)
        return result if not (isinstance(result, int) and result >= 0) else Natural(result)

    def __mul__(self, x: int):
        result = super().__mul__(x)
        return result if not (isinstance(result, int) and result >= 0) else Natural(result)

    def __mod__(self, x: int):
        result = super().__mod__(x)
        return result if not (isinstance(result, int) and result >= 0) else Natural(result)

    def __floordiv__(self, x: int):
        result = super().__floordiv__(x)
        return result if not (isinstance(result, int) and result >= 0) else Natural(result)

    def __divmod__(self, x: int):
        div, mod = super().__divmod__(x)
        d = div if not (isinstance(div, int) and div >= 0) else Natural(div)
        m = mod if not (isinstance(mod, int) and mod >= 0) else Natural(mod)

        return d, m

    def __lshift__(self, x: int): return Natural(super().__lshift__(x))
    def __rshift__(self, x: int): return Natural(super().__rshift__(x))

    def __and__(self, x: int):
        result = super().__and__(x)
        return result if not (isinstance(result, int) and result >= 0) else Natural(result)

    def __xor__(self, x: int):
        result = super().__xor__(x)
        return result if not (isinstance(result, int) and result >= 0) else Natural(result)

    def __or__(self, x: int):
        result = super().__or__(x)
        return result if not (isinstance(result, int) and result >= 0) else Natural(result)

    def __radd__(self, x: int): return self.__add__(x)

    def __rsub__(self, x: int):
        result = x - int(self)
        return result if not (isinstance(result, int) and result >= 0) else Natural(result)

    def __rmul__(self, x: int): return self.__mul__(x)

    def __rmod__(self, x: int):
        result = x % int(self)
        return result if not (isinstance(result, int) and result >= 0) else Natural(result)

    def __rfloordiv__(self, x: int):
        result = x // int(self)
        return result if not (isinstance(result, int) and result >= 0) else Natural(result)

    def __rdivmod__(self, x: int):
        div, mod = divmod(x, int(self))
        d = div if not (isinstance(div, int) and div >= 0) else Natural(div)
        m = mod if not (isinstance(mod, int) and mod >= 0) else Natural(mod)

        return d, m

    def __rlshift__(self, x: int):
        result = x << int(self)
        return result if not (isinstance(result, int) and result >= 0) else Natural(result)

    def __rrshift__(self, x: int):
        result = x >> int(self)
        return result if not (isinstance(result, int) and result >= 0) else Natural(result)

    def __rand__(self, x: int): return self.__and__(x)
    def __rxor__(self, x: int): return self.__xor__(x)
    def __ror__(self, x: int): return self.__or__(x)

    def __abs__(self): return Natural(self)
    def __pos__(self): return Natural(self)
    def __round__(self): return Natural(self)
    def __trunc__(self): return Natural(self)
    def __floor__(self): return Natural(self)
    def __ceil__(self): return Natural(self)

    def __contains__(self, digit: int): return digit in self.__digits

    raise_instead(ValueError, IndexError)
    def __getitem__(self, index: int): return self.__digits[Integral.ensure_is_between(index, -self.__length, self.__length)]

    def __len__(self): return self.__length

class NaturalType(Callable[..., Natural]):

    def __init__(self, lower_bound: Natural = 0, upper_bound: Union[None, Natural] = None):
        self.__lower = Natural(lower_bound)
        self.__upper = upper_bound if upper_bound is None else Natural(upper_bound)

        if not self.__upper is None and self.__upper < self.__lower:
            self.__lower, self.__upper = self.__upper, self.__lower

        self.__range = 'Infinity' if upper_bound is None else (self.__upper - self.__lower)

    @property
    def lower_bound(self) -> Natural: return self.__lower

    @property
    def range(self) -> Union[Natural, str]: return self.__range

    @property
    def upper_bound(self) -> Union[Natural, None]: return self.__upper

    def random(self, max_value: Union[None, Natural] = None):
         max_ = Natural(max_value) if not max_value is None else (self.__upper if not self.__upper is None else Natural.RAND_MAX)
         max_ -= self.__lower

         return randbelow(max_) + self.__lower

    def reset_lower_bound(self, new_bound: Natural):
        lower = Natural(new_bound)

        if lower > self.__upper:
            raise ValueError(':[%d]: Input exceeds given upper bound.' % lower)

        self.__lower = lower

    def reset_upper_bound(self, new_bound: Natural = None):
        upper = Natural(new_bound) if not new_bound is None else None

        if upper and (upper < self.__lower):
            raise ValueError(':[%d]: Input exceeds given lower bound.' % upper)

        self.__upper = upper

    def __call__(self, value: int):
        if value < self.__lower or (not self.__upper is None and value > self.__upper):
            raise ValueError(':[%d]: Input is outside of the range of [%d, %s.' % (value, self.__lower, '\u221E)' if self.__upper is None else (str(self.__upper) + ']')))

        return Natural(value)
