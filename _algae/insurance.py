class Integral:
    @staticmethod
    def ensure(x: int) -> int:
        if isinstance(x, int):
            return x
        elif hasattr(val, '__index__'):
            return val.__index__()
        else:
            raise TypeError(':[%s]: Input is not an integral type.' % str(x))

    @staticmethod
    def ensure_is_between(x: int, left: int, right: int, right_inclusive: bool = False) -> int:
        n_x = Integral.ensure(x)
        n_left = Integral.ensure(left)
        n_right = Integral.ensure(right)

        is_min_to_max = n_left < n_right

        if right_inclusive:
            n_right += 1 if is_min_to_max else -1

        if (is_min_to_max and (n_x >= n_left) and (n_x < n_right)) or (not is_min_to_max and (n_x <= left) and (n_x > right)):
            return n_x
        else:
            base = ':[%d]: Input is not in the range of [%d, ' % (n_x, n_left)

            if right_inclusive:
                msg = ''.join([base, '%d].' % (n_right + (-1 if is_min_to_max else 1))])
            else:
                msg = ''.join([base, '%d).' % (n_right + (-1 if is_min_to_max else 1))])

            raise ValueError(msg)

    @staticmethod
    def ensure_is_not_zero(x: int) -> int:
        n_x = Integral.ensure(x)

        if n_x != 0:
            return n_x
        else:
            raise ValueError(':[%d]: Input is zero.')

    @staticmethod
    def ensure_in_natural(x: int, zero_inclusive: bool = True) -> int:
        n_x = Integral.ensure(x)

        if n_x >= (0 if zero_inclusive else 1):
            return n_x
        else:
            raise ValueError(':[%d]: Input is less than %d.' % (0 if zero_inclusive else 1))
