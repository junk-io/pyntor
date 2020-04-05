from pyntor.pair import Pair, PairElement
from pyntor.natural import Natural
from secrets import randbelow
from typing import Callable, Sequence, Tuple

class BracketFunction:

    def __init__(self, bracket_function: Callable[[Sequence[Natural]], Pair]):
        self.__f = bracket_function

    @property
    def method(self): return self.__f

    def pair(self, sequence: Sequence[Natural]) -> Pair: return self.__f(sequence)

    def pair_random(self, length, max_value: Natural = 100):
        pair = [randbelow(max_value) for _ in range(length)]

        if len(pair) > 2:
            return Pair(*self.__f(pair))
        else:
            return Pair(pair[0], pair[1])

    def __call__(self, sequence: Sequence[Natural]) -> Pair: return Pair(*self.__f(sequence))
