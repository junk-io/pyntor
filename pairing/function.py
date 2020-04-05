from pyntor.bracket.function import BracketFunction
from pyntor.bracket.functions import LBracket
from pyntor.pair import Pair
from pyntor.natural import Natural
from secrets import randbelow
from typing import Callable, Final, Union

Encoder = Callable[[Union[Pair, tuple]], Natural]
Decoder = Callable[[Natural], Union[Pair, tuple]]

RAND_MAX: Final[int] = 100
LBRACKET: Final[LBracket] = LBracket()

class PairingFunction:

    def __init__(self, encoder: Encoder, decoder: Decoder):
        x = randbelow(RAND_MAX) + 1
        y = randbelow(RAND_MAX) + 1

        if ((b := encoder(1, 2)) == encoder (2, 1)) or ((n := encoder(x, y)) == encoder(y, x)):
            raise ValueError('Non-unique encoder.')
        elif not ((1, 2) == decoder(b) and (x, y) == decoder(n)):
            raise ValueError('Incompatible encoder and decoder.')

        self.__encoder = encoder
        self.__decoder = decoder

    @property
    def encoder(self): return self.__encoder

    @property
    def decoder(self): return self.__decoder

    def encode(self, pair: Pair) -> Natural:
        x = self.encode(pair.x) if isinstance(pair.x, Pair) else pair.x
        y = self.encode(pair.y) if isinstance(pair.y, Pair) else pair.y

        return Natural(self.__encoder(x, y))

    def decode(self, n: Natural) -> Pair: return Pair(*self.__decoder(n))
