from pyntor.bracket.function import BracketFunction
from pyntor.pair import Pair, PairElement
from pyntor.natural import Natural
from typing import Tuple

class LBracket(BracketFunction):

    __instance = None

    def __new__(cls):
        if LBracket.__instance is None:
            LBracket.__instance = BracketFunction.__new__(cls)

        return LBracket.__instance

    def __init__(self):
        def method(sequence):
            pair = Pair(sequence[0], sequence[-1])

            for i in range(1, (len(sequence) - 1)):
                pair = Pair(Pair(pair.x, sequence[i]), pair.y)

            return pair

        super().__init__(method)

        del method

class PLBracket(BracketFunction):

    __instance = None

    def __new__(cls):
        if PLBracket.__instance is None:
            PLBracket.__instance = BracketFunction.__new__(cls)

        return PLBracket.__instance

    def __init__(self):
        def method(sequence):
            pair = Pair(sequence[0], sequence[-1])

            for i in range(1, (len(sequence) - 1)):
                if isinstance(pair.x, Natural):
                    pair = Pair(Pair(pair.x, sequence[i]), pair.y)
                else:
                    if isinstance(pair.x.y, Natural):
                        pair = Pair(Pair(pair.x.x, Pair(pair.x.y, sequence[i])), pair.y)
                    else:
                        pair = Pair(Pair(pair.x, sequence[i]), pair.y)
            return pair

        super().__init__(method)

        del method

class LRBracket(BracketFunction):

    __instance = None

    def __new__(cls):
        if LRBracket.__instance is None:
            LRBracket.__instance = BracketFunction.__new__(cls)

        return LRBracket.__instance

    def __init__(self):
        def method(sequence):
            pair = Pair(sequence[0], sequence[-1])
            pair_x = True

            for i in range(1, (len(sequence) - 1)):
                if pair_x:
                    pair = Pair(Pair(pair.x, sequence[i]), pair.y)
                    pair_x = False
                else:
                    pair = Pair(pair.x, Pair(sequence[i], pair.y))
                    pair_x = True

            return pair

        super().__init__(method)

        del method


class PLRBracket(BracketFunction):

    __instance = None

    def __new__(cls):
        if PLRBracket.__instance is None:
            PLRBracket.__instance = BracketFunction.__new__(cls)

        return PLRBracket.__instance

    def __init__(self):
        def method(sequence):
            if len(sequence) == 2:
                return Pair(sequence[0], sequence[1])
            elif len(sequence) == 3:
                return Pair(Pair(sequence[0], sequence[1]), sequence[2])
            elif len(sequence) > 3:
                x_pair = Pair(sequence[0], sequence[1])
                y_pair = Pair(sequence[-2], sequence[-1])
                from_x = True
                unpaired = len(sequence) - 4
                i = 2
                d = -3

                while(unpaired > 1):
                    if from_x:
                        x_pair = Pair(x_pair, Pair(sequence[i], sequence[i + 1]))
                        from_x = False
                        unpaired -= 2
                        i += 2
                    else:
                        y_pair = Pair(Pair(sequence[d - 1], sequence[d]), y_pair)
                        from_x = True
                        unpaired -= 2
                        d -= 2

                if unpaired == 1:
                    if from_x:
                        x_pair = Pair(x_pair, sequence[i])
                    else:
                        y_pair = Pair(sequence[d], y_pair)

                return Pair(x_pair, y_pair)
            else:
                raise ValueError("Not enough integers in the sequence.")

        super().__init__(method)

        del(method)

class PRBracket(BracketFunction):

    __instance = None

    def __new__(cls):
        if PLBracket.__instance is None:
            PLBracket.__instance = BracketFunction.__new__(cls)

        return PLBracket.__instance

    def __init__(self):
        def method(sequence):
            pair = Pair(sequence[0], sequence[-1])

            for i in range(2, len(sequence)):
                if isinstance(pair.y, Natural):
                    pair = Pair(pair.x, Pair(sequence[-i], pair.y))
                else:
                    if isinstance(pair.y.x, Natural):
                        pair = Pair(pair.x, Pair(Pair(sequence[-i], pair.y.x), pair.y.y))
                    else:
                        pair = Pair(Pair(pair.x, sequence[i]), pair.y)
            return pair

        super().__init__(method)

        del method

class RBracket(BracketFunction):

    __instance = None

    def __new__(cls):
        if RBracket.__instance is None:
            RBracket.__instance = BracketFunction.__new__(cls)

        return RBracket.__instance

    def __init__(self):
        def method(sequence):
            pair = Pair(sequence[0], sequence[-1])

            for i in range(2, len(sequence)):
                pair = Pair(pair.x, Pair(sequence[-i], pair.y))

            return pair

        super().__init__(method)

        del method


class PRLBracket(BracketFunction):

    __instance = None

    def __new__(cls):
        if PRLBracket.__instance is None:
            PRLBracket.__instance = BracketFunction.__new__(cls)

        return PRLBracket.__instance

    def __init__(self):
        def method(sequence):
            if len(sequence) == 2:
                return Pair(sequence[0], sequence[1])
            elif len(sequence) == 3:
                return Pair(Pair(sequence[0], sequence[1]), sequence[2])
            elif len(sequence) > 3:
                x_pair = Pair(sequence[0], sequence[1])
                y_pair = Pair(sequence[-2], sequence[-1])
                from_y = True
                unpaired = len(sequence) - 4
                i = 2
                d = -3

                while(unpaired > 1):
                    if from_y:
                        y_pair = Pair(Pair(sequence[d - 1], sequence[d]), y_pair)
                        from_y = False
                        unpaired -= 2
                        d -= 2
                    else:
                        x_pair = Pair(x_pair, Pair(sequence[i], sequence[i + 1]))
                        from_y = True
                        unpaired -= 2
                        i += 2

                if unpaired == 1:
                    if from_y:
                        y_pair = Pair(sequence[d], y_pair)
                    else:
                        x_pair = Pair(x_pair, sequence[i])

                return Pair(x_pair, y_pair)
            else:
                raise ValueError("Not enough integers in the sequence.")

        super().__init__(method)

        del(method)

class RLBracket(BracketFunction):

    __instance = None

    def __new__(cls):
        if RLBracket.__instance is None:
            RLBracket.__instance = BracketFunction.__new__(cls)

        return RLBracket.__instance

    def __init__(self):
        def method(sequence):
            pair = Pair(sequence[0], sequence[-1])
            pair_y = True

            for i in range(1, (len(sequence) - 1)):
                if pair_y:
                    pair = Pair(pair.x, Pair(sequence[i], pair.y))
                    pair_y = True
                else:
                    pair = Pair(Pair(pair.x, sequence[i]), pair.y)
                    pair_y = False

            return pair

        super().__init__(method)

        del method

class Log2Bracket(BracketFunction):

    __instance = None

    def __new__(cls):
        if Log2Bracket.__instance is None:
            Log2Bracket.__instance = BracketFunction.__new__(cls)

        return Log2Bracket.__instance

    def __init__(self):
        def method(sequence):
            def split(sequence):
                half = len(sequence) // 2 if (len(sequence) & 1) == 0 else (len(sequence) + 1) // 2

                x = sequence[:half]
                y = sequence[half:]

                if len(x) == 1:
                    pair_x = x[0]
                    pair_y = split(y) if len(y) > 1 else y[0]
                else:
                    pair_x = split(x)
                    pair_y = split(y) if len(y) > 1 else y[0]

                return Pair(pair_x, pair_y)
            return split(sequence)

        super().__init__(method)

        del method

class PyramidBracket(BracketFunction):

    __instance = None

    def __new__(cls):
        if PyramidBracket.__instance is None:
            PyramidBracket.__instance = BracketFunction.__new__(cls)

        return PyramidBracket.__instance

    def __init__(self):
        def method(sequence):
            length = len(sequence)
            end = (length - 1) if (length & 1) == 0 else (length - 2)

            pairs = [Pair(sequence[i], sequence[i+1]) for i in range(0, end, 2)]

            if end == (length - 2):
                pairs.append(sequence[-1])

            while len(pairs) > 1:
                length = len(pairs)
                end = (length - 1) if (length & 1) == 0 else (length - 2)

                new_pairs = [Pair(pairs[i], pairs[i+1]) for i in range(0, end, 2)]

                if end == (length - 2):
                    new_pairs.append(pairs[-1])

                pairs = new_pairs

            return Pair(*pairs[0])

        super().__init__(method)

        del method
