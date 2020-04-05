from math import floor, sqrt
from pyntor._algae import math as pmath
from pyntor._algae.common import swap_if
from pyntor.pairing.function import PairingFunction

class CantorPairing(PairingFunction):

    __instance = None

    def __new__(cls):
        if CantorPairing.__instance is None:
            CantorPairing.__instance = PairingFunction.__new__(cls)

        return CantorPairing.__instance

    def __init__(self):
        encoder = lambda x, y: pmath.tn(x + y) + y

        def decoder(n):
            w = int(floor((sqrt(8*n + 1) - 1) / 2))
            t = pmath.tn(w)

            return w - n + t, n - t

        super().__init__(encoder, decoder)

        del decoder

class GodelPairing(PairingFunction):

    __instance = None

    def __new__(cls):
        if GodelPairing.__instance is None:
            GodelPairing.__instance = PairingFunction.__new__(cls)

        return GodelPairing.__instance

    def __init__(self):
        encoder = lambda x, y: (1 << x) * (3 ** y)

        def decoder(n):
            if n == 0:
                raise ValueError('Zero is not a valid input.')

            r, w = pmath.divide_out_and_count(n, 6)
            x, y = (pmath.filog2(r) + w, w) if (r & 1) == 0 else (w, pmath.filog3(r) + w)

            return x, y

        super().__init__(encoder, decoder)

        del decoder

class PeterPairing(PairingFunction):

    __instance = None

    def __new__(cls):
        if PeterPairing.__instance is None:
            PeterPairing.__instance = PairingFunction.__new__(cls)

        return PeterPairing.__instance

    def __init__(self):
        def encoder(x, y):
            m, n = pmath.max_min(x, y)
            f = 0 if m == y else 1

            return (m ** 2) + (2 * n) + f

        def decoder(n):
            x, z = pmath.root_square_difference(n)
            y = z >> 1

            return swap_if(x, y, pmath.is_even(z))

        super().__init__(encoder, decoder)

        del encoder, decoder

class QPairing(PairingFunction):

    __instance = None

    def __new__(cls):
        if QPairing.__instance is None:
            QPairing.__instance = PairingFunction.__new__(cls)

        return QPairing.__instance

    def __init__(self):
        encoder = lambda x, y: (1 << y) * ((2 * x) + 1) - 1

        def decoder(n):
            w, y = pmath.divide_out_and_count(n + 1, 2)
            return (w - 1) // 2, y

        super().__init__(encoder, decoder)

        del decoder

class RosenbergStrongPairing(PairingFunction):

    __instance = None

    def __new__(cls):
        if RosenbergStrongPairing.__instance is None:
            RosenbergStrongPairing.__instance = PairingFunction.__new__(cls)

        return RosenbergStrongPairing.__instance

    def __init__(self):
        def encoder(x, y):
            m = max(x, y)
            return (m * (m + 1)) + x - y

        def decoder(n):
            w, z = pmath.root_square_difference(n)

            if z < w:
                x, y = z, w
            else:
                x = w
                y  = (w * (w + 2)) - n

            return x, y

        super().__init__(encoder, decoder)

        del encoder, decoder

class SquarePairing(PairingFunction):

    __instance = None

    def __new__(cls):
        if SquarePairing.__instance is None:
            SquarePairing.__instance = PairingFunction.__new__(cls)

        return SquarePairing.__instance

    def __init__(self):
        def encoder(x, y):
            m = max(x, y)
            n = m ** 2

            return (n + y - x) if m == y else (n + (2*x) - y)

        def decoder(n):
            w, z = pmath.root_square_difference(n)

            if z == w:
                x, y = w, z
            elif z < w:
                x, y = (w - z), w
            else:
                x, y = w, (2 * w) - z

            return x, y

        super().__init__(encoder, decoder)

        del encoder, decoder
