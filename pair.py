from enum import Enum
from pyntor._algae.decorators import raise_instead
from pyntor._algae.insurance import Integral
from pyntor.natural import Natural
from secrets import randbelow
from typing import Final, List, Sequence, Tuple, Union

PairType = Union[Natural, Sequence]

class PairElement(Enum):
    X = 0
    Y = 1

    def __repr__(self): return '.x' if self == PairElement.X else '.y'

    def __str__(self): return self.__repr__()

class Pair:

    def __init__(self, x: PairType, y: PairType):
        def resolve(param):
            if isinstance(param, Natural):
                return param
            elif isinstance(param, Pair):
                return Pair(*param.copy())
            elif isinstance(param, Sequence) and len(param) == 2:
                return Pair(param[0], param[1])
            else:
                return Natural(param)

        self._x = resolve(x)
        self._y = resolve(y)

        del resolve

    @classmethod
    def from_tuple(cls, pair: Tuple): return cls(*pair)

    @classmethod
    def random(cls, max_x: Natural = 100, max_y: Natural = 100): return cls(randbelow(max_x), randbelow(max_y))

    @property
    def x(self): return self._x

    @property
    def y(self): return self._y

    def copy(self):
        if self.is_natural():
            x, y = self
        elif isinstance(self._x, Pair):
            x = self._x.copy()
            y = self._y.copy() if isinstance(self._y, Pair) else self._y
        else:
            x = self._x
            y = self._y.copy()

        return Pair(x, y)

    def count(self):
        count_x = 1 if isinstance(self._x, Natural) else self._x.count()
        count_y = 1 if isinstance(self._y, Natural) else self._y.count()

        return count_x + count_y

    def depth_of_x(self):
        depth = 0

        x = self._x

        while(isinstance(x, Pair)):
            x = x.x
            depth += 1

        return depth

    def depth_of_y(self):
        depth = 0

        y = self._y

        while(isinstance(y, Pair)):
            y = y.y
            depth += 1

        return depth


    def flatten(self):
        def f(pair):
            flattened = []

            for value in pair:
                if isinstance(value, Pair):
                    flattened.extend(f(value))
                else:
                    flattened.append(value)

            return flattened

        return tuple(f(self))

    def is_natural(self): return isinstance(self._x, Natural) and isinstance(self._y, Natural)

    raise_instead(ValueError, IndexError)
    def __getitem__(self, key: Union[int, PairElement, Sequence[int], Sequence[PairElement]]):

        if isinstance(key, PairElement):
            return self._x if key == PairElement.X else self._y
        elif isinstance(key, Sequence):

            pair = self

            for i in range(len(key)):
                if not isinstance(pair, Pair):
                    raise ValueError(':[%s]: Path does not exist.' % ''.join(key))

                element = PairElement(key[i])

                pair = pair.x if element == PairElement.X else pair.y

            return pair
        else:
            k = Integral.ensure_is_between(key, -2, 2)

            return self._x if (k == 0 or k == -2) else self._y

    def __iter__(self):
        yield self._x
        yield self._y

    def __len__(self): return 2

    def __repr__(self):
        def stringify(pair):
            if pair.is_natural():
                return '(%d, %d)' % (pair.x, pair.y)
            else:
                x = '(%s, ' % (str(pair.x) if isinstance(pair.x, Natural) else stringify(pair.x))
                y = '%s)' % (str(pair.y) if isinstance(pair.y, Natural) else stringify(pair.y))

                return x + y

        return stringify(self)

    def __reversed__(self):
        yield self._y
        yield self._x

    def __str__(self): return self.__repr__()

class MutablePair(Pair):

    def lock(self): return Pair(*self.copy())

    def replace(self, path: Union[int, PairElement, Sequence[int], Sequence[PairElement]], new_value: Union[Natural, Pair]):
        if isinstance(new_value, Pair) or (isinstance(new_value, tuple) and len(new_value) == 2):
            value = Pair(*new_value)
        else:
            value = Natural(new_value)

        if not isinstance(path, Sequence):
            if PairElement(path) == PairElement.X:
                self._x = value
            else:
                self._y = value
        else:
            pair = self[path[:-1]]

            if PairElement(path[-1]) == PairElement.X:
                pair._x = value
            else:
                pair._y = value

    def __setitem__(self, path: Union[PairElement, Sequence[PairElement]], new_value: Union[Natural, Pair]):

        return self.replace(path, new_value)
