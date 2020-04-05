from typing import Any

def choose(x: Any, y: Any, condition: bool): return y if condition else x

def swap_if(x: Any, y: Any, condition: bool): return (y, x) if condition else (x, y)
