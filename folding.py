from pyntor.natural import Natural

def fold(value: int) -> Natural: return Natural(2 * value) if value >= 0 else Natural((2 * abs(value)) - 1)

def unfold(value: Natural) -> int: return -((value + 1) // 2) if (value & 1) == 1 else (value // 2)
