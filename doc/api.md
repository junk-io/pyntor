<span style="font-family: Consolas, monospace">

- [1 Introduction](#1-introduction)
- [2 Natural(int)](#2-naturalint)
  - [Overview](#overview)
  - [Module](#module)
- [3 NaturalType](#3-naturaltype)
  - [Overview](#overview-1)
  - [Module](#module-1)
- [4 Folding](#4-folding)
  - [Overview](#overview-2)
  - [Module](#module-2)
- [5 PairElement(Enum)](#5-pairelementenum)
  - [Overview](#overview-3)
  - [Module](#module-3)
- [6 Pair](#6-pair)
  - [Overview](#overview-4)
  - [Module](#module-4)
  - [Implementations](#implementations)
- [7 MutablePair(Pair)](#7-mutablepairpair)
  - [Overview](#overview-5)
  - [Module](#module-5)
- [8 BracketFunction](#8-bracketfunction)
  - [Overview](#overview-6)
  - [Module](#module-6)
  - [Implementations](#implementations-1)
- [9 Bracket Functions](#9-bracket-functions)
- [10 PairingFunction](#10-pairingfunction)
  - [Overview](#overview-7)
  - [Module](#module-7)
- [11 Pairing Functions](#11-pairing-functions)
  - [Overview](#overview-8)
  - [CantorPairing](#cantorpairing)
  - [GodelPairing](#godelpairing)
  - [PeterPairing](#peterpairing)
  - [QPairing](#qpairing)
  - [RosenbergStrongPairing](#rosenbergstrongpairing)
  - [SquarePairing](#squarepairing)
- [Examples](#examples)
  - [<u>**A First Example**</u>](#ua-first-exampleu)
  - [<u>**Encoding Negative Numbers**</u>](#uencoding-negative-numbersu)

<br>

<br>

# 1 Introduction

`pyntor` is a small [pairing function](https://en.wikipedia.org/wiki/pairing_function) library. 

A pairing function is a bijection of *N<sup>2</sup>* &rarr; *N*, where *N* is the set of nonnegative integers.

`pyntor` implements four main types:

* `Natural`
  * A nonnegative integer
* `Pair`
  * A 2-tuple where each element is either a `Natural` or another `Pair`
* `BracketFunction`
  * A function that transforms a sequence of `Natural` into a `Pair`
* `PairingFunction`
  * A function that encodes a pair of `Natural` into a single `Natural`

<br>

# 2 Natural(int)

```py
>>> from pyntor.natural import Natural
```
<br>

## Overview

---

`Natural` is a class that represents an indexable nonnegative integer. It inherits from `int` and is compatible with any method taking an `int` as input. Arithmetic gives precedence to the *type that can hold the result*.

<br>

## Module

---

### **Natural.RAND_MAX** <!-- omit in toc -->

> * *Final[Natural]*
> 
>	* The default maximum for random values set to `2`<sup>`31`</sup> `= 2147483648` 
 
---
### **Natural.\_\_init\_\_(self, value = 0)** <!-- omit in toc -->

> Parameters:
> 
> * value : *int, str, Sequence[int]*
> 
> 	* A nonnegative integer. Default is 0

> Exceptions:
> 
> * *TypeError*
> 	* `value` is not one of the listed types
> 
> * *ValueError*
> 	* `value` is negative

<br>

```py
>>> x = Natural(1)
```
---

### **Natural.random(cls, max_value = 100)** <!-- omit in toc -->

> Decorators:
> 
> * @classmethod

> Parameters:
> 
> * max_value: *Natural*
> 
> 	* The exclusive upper bound for the value

> Returns:
> 
> * *Natural*
> 
>	* A random integer in the range [0, `max_value`)

---

### **Natural.naturalize(values)** <!-- omit in toc -->

> Decorators:
> 
> * @staticmethod

> Parameters:
> 
> * values: *Iterable*
> 
> 	* A list of nonnegative integers

> Returns:
> 
> * *Iterable*
> 
> 	* A list where every element of the input is cast as a `Natural`

> Comments:
> 
> * Elements of the input can be of any form valid as input to the constructor of `Natural`

<br>

```py
>>> sequence = [1, '2', 3, (4, 5), 6, 7, '89']
>>> natural_sequence = Natural.naturalize(sequence)
>>> natural_sequence
[1, 2, 3, 45, 6, 7, 89]
```

---

### **Natural.naturals(start, end=None, step=1)** <!-- omit in toc -->

> Decorators:
> 
> * @staticmethod

> Parameters:
> 
> * start: *int*
> 	* The starting value of the list or the length of the list if `end` is `None`
> 
> * end: *int*, *None*
> 	* If not `None`, it is the excluded upper bound of the list
> 
> * step:
> 	* The difference between each successive value in the list

> Returns:
> 
> * *Sequence*
> 
> 	* A sequence of `Natural` numbers

<br>

```py
>>> sequence1 = Natural.naturals(10)
>>> sequence2 = Natural.naturals(10, 0)
>>> sequence3 = Natural.naturals(0, 100, 11)
>>> zeroes = Natural.naturals(1) * 10
>>> ones = Natural.naturals(1, 2) * 10
>>> 
>>> sequence1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> sequence2
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> sequence3
[0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> zeroes
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> ones
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```

---

### **Natural.random_sequence(length, max_value = 100)** <!-- omit in toc -->

> Decorators:
> 
> * @staticmethod

> Parameters:
>
> * length: *Natural*
> 	* The length of the produced sequence
> 
> * max_value: *Natural*
> 	* The exclusive upper bound for the values in the sequence

> Returns:
> 
> * *Sequence[Natural]*
> 
>	* A random sequence of `Natural` numbers

---

### **Natural.repeat(value, count)** <!-- omit in toc -->

> Decorators:
> 
> @staticmethod

> Parameters:
> 
> * value: *int*
> 	* The value to be repeated
> 
> * count: *int*
> 	* The number of times to repeat the value

> Returns:
> 
> * *Sequence*
> 
> 	* A list with `value` repeated `count` times

<br>

```py
>>> zeroes = Natural.repeat(0, 10)
>>> ones = Natural.repeat(1, 10)
>>> 
>>> zeroes
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> ones
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```
---

### **Natural.digits** <!-- omit in toc -->

> Decorators:
> 
> * @property

> Returns:
> 
> * *Tuple*
> 
> 	* The digits in this integer

<br>

```py
>>> x = Natural(12345)
>>> sum(x.digits)
15
>>> y = Natural(1239586732983)
>>> unique_digits = set(y.digits)
>>> 
>>> unique_digits
{1, 2, 3, 5, 6, 7, 8, 9}
```

---

### **Natural.count(self, digit)** <!-- omit in toc -->

> Parameters:
> 
> * digit: *int*
> 
> 	* The digit to count in this integer

> Returns:
> 
> * *Natural*
> 
> 	* The number of times `digit` appears in this integer

```py
>>> x = Natural(1239586732983)
>>> unique_digits = set(y.digits)
>>> digit_counts = {digit, y.count(digit) for digit in unique_digits}
>>> 
>>> digit_counts
{1: 1, 2: 2, 3: 3, 5: 1, 6: 1, 7: 1, 8: 2, 9: 2}
```

---

### **Natural.\_\_add\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_radd\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_sub\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_rsub\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_mul\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_rmul\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_mod\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_rmod\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_floordiv\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_rfloordiv\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_and\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_rand\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_xor\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_rxor\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_or\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_ror\_\_(self, x)** <!-- omit in toc -->

> Parameter:
> 
> * x: *int*, *float*
> 
>	* The second operand

> Returns:
> 
> * *Natural*
> 	* If the result of the operation is a positive integer
> 
> * *int*, *float*
> 	* If the result of the operation is a negative integer or float, respectively

<br>

```py
>>> x = Natural(1)
>>> y = Natural(2)
>>> p = x + y
>>> m = x - y
>>> d = x / y
>>> f = x // y
>>> 
>>> p
3
>>> m
-1
>>> d
0.5
>>> f
0
>>> type(p)
<class 'pyntor.natural.natural.Natural'>
>>> type(m)
<class 'int'>
>>> type(d)
<class 'float'>
>>> type(f)
<class 'pyntor.natural.natural.Natural'>
```
---

### **Natural.\_\_lshift\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_rlshift\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_rshift\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_rrshift\_\_(self, x)** <!-- omit in toc -->

> Parameter:
> 
> * x: *int*
> 
>	* The shift amount

> Returns:
> 
> * *Natural*
> 
> 	* If the result shifting this integer by `x`

<br>

```py
>>> Natural(1) << 4
16
>>> 75 >> Natural(2)
18
```

---

### **Natural.\_\_divmod\_\_(self, x)** <!-- omit in toc -->
### **Natural.\_\_rdivmod\_\_(self, x)** <!-- omit in toc -->

> Parameter:
> 
> * x: *int*, *float*
> 
>	* The second operand

> Returns:
> 
> * *Tuple*
> 
> 	* `div` and `mod` will be either a `Natural` if their results are positive integers, or an `int` otherwise

<br>

```py
>>> divmod(Natural(71), Natural(5))
(14, 1)
```

---

### **Natural.\_\_abs\_\_(self)** <!-- omit in toc -->
### **Natural.\_\_pos\_\_(self)** <!-- omit in toc -->
### **Natural.\_\_round\_\_(self)** <!-- omit in toc -->
### **Natural.\_\_trunc\_\_(self)** <!-- omit in toc -->
### **Natural.\_\_floor\_\_(self)** <!-- omit in toc -->
### **Natural.\_\_ceil\_\_(self)** <!-- omit in toc -->

> Returns:
> 
> * *Natural*
> 
> 	* This integer

---

### **\_\_contains\_\_(self, digit: int)** <!-- omit in toc -->

> Parameters:
> 
> * digit: *int*
> 
> 	* The digit to search for in this integer

> Returns:
> 
> * *bool*
> 
> 	* Whether or not this integer contains `digit`

<br>

```py
>>> x = Natural(12345)
>>> 3 in x
True
>>> 6 in x
False
```

---

### **\_\_getitem\_\_(self, index: int)** <!-- omit in toc -->

> Decorators:
> 
> * @raise_instead(ValueError, IndexError)
> 
> 	* When a `ValueError` is raised it is excepted and an `IndexError` is raised instead

> Parameters:
> 
> * index: *int*
> 
> 	* The index of the digit to return

> Returns:
> 
> * *Natural*
> 
> 	* The digit in the 10<sup>`index`</sup> position if `index` is a nonnegative integer, otherwise the digit in the 10<sup>`len + index` position

<br>

```py
>>> x = Natural(12345)
>>> x[0]
5
>>> x[1]
4
>>> x[-1]
1
```

---

### **\_\_len\_\_(self)** <!-- omit in toc -->

> Returns:
> 
> * *Natural*
> 
> 	* The number of digits in this integer.

<br>

```py
>>> x = Natural(123456789876543210)
>>> len(x)
18
```

---

<br>

# 3 NaturalType

```py
>>> from pyntor.natural import NaturalType
```

<br>

## Overview

---

`NaturalType` provides a means of creating a *"type"* of `Natural` that exists within given bounds. `NaturalType` is thus, a producer of `Natural` objects. `Natural` can be thought of as a `NaturalType` with a lower bound of `0` and no upper bound.

<br>

## Module

---

### **NaturalType.\_\_init\_\_(self, lower_bound = 0, upper_bound = None)** <!-- omit in toc -->

> Parameters:
> 
> * lower_bound: *Natural*
> 	* The lower bound of this type. Default is `0`
> 
> * upper_bound: *Natural*, *None*
> 	* The optional exclusive upper bound of this type. Default is `None`

<br>

```py
>>> natural1 = NaturalType(lower_bound=1)
```

---

### **NaturalType.lower_bound** <!-- omit in toc -->

> Decorators:
> 
> * @property

> Returns:
> 
> * *Natural*
> 
> 	* The lower bound of this type

---

### **NaturalType.upper_bound** <!-- omit in toc -->

> Decorators:
> 
> * @property

> Returns:
> 
> * *Natural*, *None*
>
>	* The excluded upper bound of this type, if one is set

---

### **NaturalType.range** <!-- omit in toc -->

> Decorators:
> 
> * @property

> Returns:
> 
> * *Natural*, *str*
>
>	* The difference between `NaturalType.upper_bound` and `NaturalType.lower_bound`, if an upper bound is set, otherwise `'Infinity'`

<br>

```py
>>> n1 = NaturalType(1)
>>> n_0_100 = NaturalType(upper_bound=100)
>>> n1.range
'Infinity'
>>> n_0_100.range
100
```

---

### **NaturalType.random(self, max_value=None)** <!-- omit in toc -->

> Parameters:
> 
> * max_value:
> 
>	* The optional exclusive upper bound for this value.

> Returns
> 
> * *Natural*
>
>	* A `Natural` number in the range [`Natural.lower_bound`, (`max_value` | NaturalType.upper_bound | `Natural.RAND_MAX`))

---

### **NaturalType.reset_lower_bound(self, new_value = 0)** <!-- omit in toc -->

> Parameters:
> 
> * new_value: *Natural*
> 
>	* The optional new lower bound of this type. Resets to `0` if no input is provided.

> Exceptions:
> 
> * ValueError
> 
> 	* If `new_value` exceeds `NaturalType.upper_bound`

<br>

```py
>>> ntype = NaturalType(upper_bound=9)
>>> ntype.lower_bound
0
>>> ntype.reset_lower_bound(4)
>>> ntype.lower_bound
4
>>> ntype.reset_lower_bound()
>>> ntype.lower_bound
0
```
---

### **NaturalType.reset_upper_bound(self, new_value = None)** <!-- omit in toc -->

> Parameters:
> 
> * new_value: *Natural*
> 
>	* The optional new upper bound of this type. Resets to `None` if no input is provided.

> Exceptions:
> 
> * ValueError
> 
> 	* If `new_value` is less than `NaturalType.lower_bound`

<br>

```py
>>> ntype = NaturalType(upper_bound=9)
>>> ntype.range
10
>>> ntype.reset_upper_bound(99)
>>> ntype.range
100
>>> ntype.reset_upper_bound()
>>> ntype.range
'Infinity'
```

---

### **NaturalType.\_\_call\_\_(self, value)** <!-- omit in toc -->

> Parameters:
> 
> * value: *int*
> 
>	* A non-negative integer in the range of `NaturalType.lower_bound` and `NaturalType.upper_bound` inclusive

> Returns:
> 
> * *Natural*
> 
>	The value as a `Natural`

> Exceptions:
> 
> * ValueError
> 
> 	* If `value` is not within the range of this type

<br>

```py
>>> ntype = NaturalType(1, 100)
>>> x = ntype(50)
>>> x
50
>>> type(x)
<class 'pyntor.natural.natural.Natural'>
>>> y = ntype(101)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "\pyntor\pyntor\natural\naturaltype.py", line 44, in __call__
    return Natural(value)
ValueError: :[101]: Input is outside of the range of [1, 100].
```

---

<br>

# 4 Folding

```py
from pyntor.folding import fold, unfold
```

<br>

## Overview

---

`folding` is a module with two methods `fold` and `unfold`. `fold` implements a simple [folding function](https://mathworld.wolfram.com/FoldingFunction.html) for allowing negative numbers to be encoded as natural numbers. `unfold` reverses the process, encoding a natural number as an integer.

<br>

## Module

---

### **fold(value)** <!-- omit in toc -->

> Parameters:
> 
> * value: *int*
> 
>	* An integer to be encoded

> Returns:
> 
> * *Natural*:
> 
>	* The integer encoded as a nonnegative integer

<br>

```py
>>> fold(0)
0
>>> fold(-1)
1
>>> fold(1)
2
>>> fold(-77)
153
```

---

### **unfold(value)** <!-- omit in toc -->

> Parameters:
> 
> * value: *Natural*
> 
>	* An nonnegative integer to be decoded

> Returns:
> 
> * *Natural*:
> 
>	* The integer corresponding to the `Natural` number

<br>

```py
>>> unfold(1)
-1
>>> unfold(32)
16
>>> unfold(67)
-34
```

---

<br>

# 5 PairElement(Enum)

```py
>>> from pyntor.pair import PairElement
```

<br>

## Overview

---

Simple enum with two possible values: 'X' and 'Y'. It can be used to build a path to elements in nested pairs.

<br>

## Module

---

### **PairElement.X** <!-- omit in toc -->

> Description:  
> 
> * Represents the 'X' or first element of a pair.

### **PairElement.Y** <!-- omit in toc -->

> Description:  
> 
> * Represents the 'Y' or second element of a pair.

<br>

```py
>>> PairElement.X
.x
>>> PairElement.Y
.y
```

---

<br>

# 6 Pair

```py
>>> from pyntor.pair import Pair
```

<br>

## Overview

---

A `Pair` is a tuple of two elements 'x' and 'y' that can either be a non-negative integer or another `Pair`.

<br>

## Module

### **Pair.\_\_init\_\_(self, x, y)** <!-- omit in toc -->

> Parameters:
> 
> * x: *Natural*, *Sequence*, *Pair*
> 	* The 'x' element of the pair
> 
> * y: *Natural*, *Sequence*, *Pair*
> 	* The 'y' element of the pair

> Comments:
> 
> * If `x` or `y` is a `Sequence`, it must have length 2 in order to be split into a pair. Any other length will be taken as the digits of an integer when passed to `Natural`. To pass a two digit number by digit into `Pair` without splitting it, prepend a `0` to the sequence

<br>

```py
>>> Pair(1, 2)
(1, 2)
>>> Pair(1, (2, Pair(3, (4, Pair(5, ((0, 6, 7), (8, 9)))))))
(1, (2, (3, (4, (5, (67, (8, 9)))))))
```

---

### **Pair.from_tuple(cls, pair)** <!-- omit in toc -->

> Parameters:
> 
> * pair: *Tuple*, *Pair*
> 
> 	* A 2-tuple where the elements are either `Natural` numbers or another 2-tuple

> Returns:
> 
> * *Pair*
> 
>	  * A copy of the pair as a `Pair`

---

### **Pair.random(cls, max_value_x = 100, max_value_y = 100)** <!-- omit in toc -->

> Decorators:
> 
> * @classmethod

> Parameters:
> 
> * max_value_x: *Natural*
> 
>	* The max value for the first element. Default is `100`
>
> * max_value_y: *Natural*
> 
>	* The max value for the second element. Default is `100`

> Returns:
> 
> * *Pair*
> 
>	* A pair of random non-negative integers

---

### **Pair.x** <!-- omit in toc -->

> Decorators:
> 
> * @property

> Returns:
> 
> * *Natural*, *Pair*
> 	* The first element of this pair

---

### **Pair.y** <!-- omit in toc -->

> Decorators:
> 
> * @property

> Returns:
> 
> * *Natural*, *Pair*
> 	* The second element of this pair

---

### **Pair.copy(self)** <!-- omit in toc -->

> Returns:
> 
> * *Pair*
> 
>	* A deep copy of this pair

<br>

```py
>>> pair = Pair((0, 1), (2, 3))
>>> pair2 = Pair(*pair)
>>> pairc = pair.copy()
>>> 
>>> pair == pair2
False
>>> pair == pairc
False
>>> 
>>> pair.x == pair2.x
True
>>> pair.x == pairc.x
False
>>> 
>>> pair.y == pair2.y
True
>>> pair.y == pair.c.y
False
```

---

### **Pair.count(self)** <!-- omit in toc -->

> Returns:
> 
> *Natural*
> 
>	* The length of the flattened sequence of this pair

<br>

```py
>>> pair = Pair(1, (2, Pair(3, (4, Pair(5, ((0, 6, 7), (8, 9)))))))
>>> pair.count()
8
```

---

### **Pair.depth_of_x(self)** <!-- omit in toc -->

> Returns:
> 
> *Natural*
> 
>	* Counts the number of times `Pair.x` can be called before reaching a `Natural`

<br>

```py
>>> pair.depth_of_x()
1
>>> pair.x
1
```

---

### **Pair.depth_of_y(self)** <!-- omit in toc -->

> Returns:
> 
> *Natural*
> 
>	* Counts the number of times `Pair.y` can be called before reaching a `Natural`

<br>

```py
>>> pair.depth_of_y()
7
>>> pair.y.y.y.y
(5, (67, (8, 9)))
```

---

### **Pair.flatten(self)** <!-- omit in toc -->

> Returns:
> 
> * *Tuple*
> 
> 	* A flattened tuple of this pair

<br>

```py
>>> pair.flatten()
(1, 2, 3, 4, 5, 67, 8, 9)
```

---

### **Pair.is_natural(self)** <!-- omit in toc -->

> Returns:
> 
> * *bool*
> 
>	* Whether or not both `Pair.x` and `Pair.y` are `Natural` instances.

<br>

```py
>>> n_pair = Pair(0, 1)
>>> pair.is_natural()
False
>>> n_pair.isnatural()
True
```

---

### **Pair.\_\_getitem\_\_(self, key)** <!-- omit in toc -->

> Decorators:
> 
> * @raise_instead(ValueError, IndexError)
> 
> 	* When a `ValueError` is raised it is excepted and an `IndexError` is raised instead

> Parameters:
> 
> * key: 
> 
>	* *int*
>		* Either `-2`, `-1`, `0`, or `1`, where `0` and `-2` represent `Pair.x` and `1` and `-1`, `Pair.y`
> 
>	* *PairElement*
>		* The element to retrieve
> 
>	* *Sequence[PairElement]*
>		* The path of the element to retrieve
>
>	* *Sequence[int]*
>		* A sequence of `0`s and `1`s, where `0` represents the `Pair.x` and `1`, `Pair.y`

> Returns:
> 
> * *Natural*
> 
>	* The element at the position of the `key`

> Exceptions:
> 
> * ValueError
> 
>	* If the int is not one of the allowed values
>	* If a member of the key is not a `PairElement`
>	* If the path does not exist for the pair

<br>

```py
>>> pair[1]
(2, (3, (4, (5, (67, (8, 9))))))
>>> 
>>> pair[1][1][1][1][1]
(67, (8, 9))
>>> 
>>> pair[PairElement.X]
1
>>> 
>>> pair[[PairElement.Y, PairElement.Y, PairElement.X]]
3
```

---

### **Pair.\_\_iter\_\_(self):** <!-- omit in toc -->

> Returns:
> 
> The first element, then the second

---

### **Pair.\_\_reversed\_\_(self):** <!-- omit in toc -->

> Returns:
> 
> The second element, then the first

---

<br>

## Implementations

---

* `MutablePair`

---

<br>

# 7 MutablePair(Pair)

```py
>>> from pyntor.pair import MutablePair
```

<br>

## Overview

---

`MutablePair` is exactly that, it's a pair that allows it's own elements or those of it's nested pairs to be replaced. 

<br>

## Module

---

### **MutablePair.lock(self)** <!-- omit in toc -->

> Returns
> 
> * *Pair*
>
>	* An immutable copy of this pair

---

### **MutablePair.replace(self, path, new_value)** <!-- omit in toc -->

> Parameters:
> 
> * path: *PairElement*, *int*, *Sequence[PairElement]*, *Sequence[int]*
> 
>	* The path to the element to be replaced
> 
> * new_value: *Natural*, *Pair*
> 
>	* The new value to replace the element with

<br>

```py
>>> from pyntor.brackets.pair import PairElement as pe
>>> pair = MutablePair(1, (2, (3, (3, 5))))
>>> pair
(1, (2, (3, (3, 5))))
>>> pair.replace([pe.Y, pe.Y, pe.X], 2)
>>> pair
(1, (2, (2, (3, 5))))
>>> pair.replace([1, 0], 1)
>>> pair
(1, 1, (2, (3, 5)))
```

---

### **MutablePair.\_\_setitem\_\_(self, path, new_value)** <!-- omit in toc -->

> Parameters:
> 
> * path: *PairElement*, *int*, *Sequence[PairElement]*, *Sequence[int]*
> 
>	* The path to the element to be replaced
> 
> * new_value: *Natural*, *Pair*
> 
>	* The new value to replace the element with

<br>

```py
>>> pair[0] = 0
>>> pair
(0, (1, (2, (3, 5))))
>>> pair[[1, 1, 1, 1]] = 4
>>> pair
(0, (1, (2, (3, 4))))
```

---

<br>

# 8 BracketFunction

```py
>>> from pyntor.bracket.function import BracketFunction
```

<br>

## Overview

---

`BracketFunction` represents a function that takes as input a sequence of integers and produces a pair. The purpose of this class and it's use is to provide a means of determining which elements should be paired together as input to a *pairing function*. This in turn, allows any pairing function to be used to transform any n-input sequence.

<br>

## Module

---

### **BracketFunction.\_\_init\_\_(self, method)** <!-- omit in toc -->

> Parameters:
> 
> * method: *Callable*
> 
>	* The function responsible for systematically pairing the elements of a sequence. The output of the function should be a `Pair`

<br>

```py
>>> def method(sequence):
		pair = Pair(sequence[0], sequence[-1])

		for i in range(1, (len(sequence) - 1)):
			pair = Pair(Pair(pair.x, sequence[i]), pair.y)

		return pair

>>> bracket = BracketFunction(method)
```

---

### **BracketFunction.method** <!-- omit in toc -->

> Decorators:
> 
> * @property

> Returns:
> 
> * *Callable*
> 
>	* The wrapped transformation function

---

### **BracketFunction.pair(self, sequence)** <!-- omit in toc -->

> Parameters:
> 
> * sequence: *Sequence[Union[Natural, Pair]]*
> 
>	* The sequence to transform into a pair

> Returns:
> 
> * *Pair*
> 
>	* A pair with elements that are either an element of the input sequence, or a pair containing pairs of them

<br>

```py
>>> seq = [i for i in range(5)]
>>> seq
[0, 1, 2, 3, 4]
>>> bracket.pair(seq)
((((0, 1), 2), 3), 4)
```

---

### **BracketFunction.pair_random(self, length, max_value = 100)** <!-- omit in toc -->

> Parameters:
> 
> * length: *Natural*
> 	* The length of the flattened sequence
> 
> * max_value: *Natural*
> 	* The maximum value for each element in the sequence. Default is `100`
> 
> * bracket_function: *BracketFunction*
> 	* The function that transforms the sequence into a `Pair`. Default is the `LBracket` function

> Returns:
> 
> * *Pair*
> 
>	* A pair of nested pairs containing the random elements in the sequence

---

### **BracketFunction.\_\_call\_\_(self, sequence)** <!-- omit in toc -->

> Parameters:
> 
> * sequence: *Sequence[Union[Natural, Pair]]*
> 
>	* The sequence to transform into a pair

> Returns:
> 
> * *Pair*
> 
>	* A pair with elements that are either an element of the input sequence, or a pair containing pairs of them

<br>

```py
>>> seq = [i for i in range(5)]
>>> seq.extend([(5, 6), (7, (8, 9))])
>>> seq
[0, 1, 2, 3, 4, (5, 6), (7, (8, 9))]
>>>
>>> bracket(seq)
((((((0, 1), 2), 3), 4), (5, 6)), (7, (8, 9)))
```

---

<br>

## Implementations

---

* `LBracket`
* `LRBracket`
* `PLBracket`
* `PLRBracket`
* `PRBracket`
* `PRLBracket`
* `PyramidBracket`
* `RBracket`
* `RLBracket`

---

<br>

# 9 Bracket Functions

`Pyntor` currently implements several bracket functions. The table below lists them and how they pair sequences of different lengths. Each of the bracket functions is implemented as a singleton.

<br>

|                | N = 2  | N = 3       | N = 4            | N = 5                 | N = 6 
| :------------: | :----: | :---------: | :--------------: | :-------------------: | :------------------------:  
| LBracket       | (0, 1) | ((0, 1), 2) | (((0, 1), 2), 3) | ((((0, 1), 2), 3), 4) | (((((0, 1), 2), 3), 4), 5)
| PLBracket      | (0, 1) | ((0, 1), 2) | (((0, 1), 2), 3) | (((0, 1), (2, 3)), 4) | ((((0, 1), (2, 3)), 4), 5)
| RBracket       | (0, 1) | (0, (1, 2)) | (0, (1, (2, 3))) | (0, (1, (2, (3, 4)))) | (0, (1, (2, (3, (4, 5)))))
| PRBracket      | (0, 1) | (0, (1, 2)) | (0, (1, (2, 3))) | (0, ((1, 2), (3, 4))) | (0, (1, ((2, 3), (4, 5))))
| LRBracket      | (0, 1) | ((0, 1), 2) | ((0, 1), (2, 3)) | (((0, 1), 2), (3, 4)) | (((0, 1), 2), (3, (4, 5)))
| PLRBracket     | (0, 1) | ((0, 1), 2) | ((0, 1), (2, 3)) | (((0, 1), 2), (3, 4)) | (((0, 1), (2, 3)), (4, 5))
| RLBracket      | (0, 1) | (0, (1, 2)) | ((0, 1), (2, 3)) | ((0, 1), (2, (3, 4))) | (((0, 1), 2), (3, (4, 5)))
| PRLBracket     | (0, 1) | (0, (1, 2)) | ((0, 1), (2, 3)) | ((0, 1), (2, (3, 4))) | ((0, 1), ((2, 3), (4, 5)))
| Log2Bracket    | (0, 1) | ((0, 1), 2) | ((0, 1), (2, 3)) | (((0, 1), 2), (3, 4)) | (((0, 1), 2), ((3, 4), 5))
| PyramidBracket | (0, 1) | ((0, 1), 2) | ((0, 1), (2, 3)) | (((0, 1), (2, 3)), 4) | (((0, 1), (2, 3)), (4, 5))

<br>

```py
>>> from pyntor.bracket.functions import PyramidBracket
>>> 
>>> pyb = PyramidBracket()
>>> bracket = lambda m: pyb([i for i in range(m)])
>>> 
>>> bracket(7)
(((0, 1), (2, 3)), ((4, 5), 6))
```

---

<br>

# 10 PairingFunction

```py
>>> from pyntor.pairing.function import PairingFunction
```

<br>

## Overview

---

`PairingFunction` represents just that, a function that maps a pair of non-negative integers to a single non-negative integer uniquely and reversibly.

<br>

## Module

---

### **PairingFunction.\_\_init\_\_(self, encoder, decoder)** <!-- omit in toc -->

> Parameters:
> 
> * encoder: *Callable*
> 
>	* A function that takes as input two `Natural` numbers and produces a single `Natural` number
>
> * decoder: *Callable*
> 
>	* A function that takes as input a single `Natural` number and produces a pair of `Natural` numbers

> Exceptions:
> 
> * ValueError
> 
>	* If `encoder(x, y)` equals `encoder(y, x)` for a random pair `(x, y)`
>
>	* If `decoder(encoder(x, y))` does not equal `(x, y)`

<br>

```py
>>> def cantor_enc = lambda x, y: (((x + y) * (x + y + 1)) // 2) + y
>>> def cantor_dec(n):
		w = int((sqrt(8*n + 1) - 1) / 2)
		t = (w * (w + 1)) // 2

		return w - n + t, n - t

>>> cantor = PairingFunction(cantor_enc, cantor_dec)
```

---

### **PairingFunction.encoder** <!-- omit in toc -->

> Decorators:
> 
> @property

> Returns
> 
> * *Callable*
> 
>	* The function that encodes a pair of integers as a single integer

---

### **PairingFunction.decoder** <!-- omit in toc -->

> Decorators:
> 
> @property

> Returns
> 
> * *Callable*
> 
>	* The function that decodes a single integer into a pair of integers

---

### **PairingFunction.encode(self, pair)** <!-- omit in toc -->

> Parameters:
> 
> * pair: *Pair*
> 
>	* The pair to be encoded

> Returns:
> 
> * *Natural*
> 
>	* The unique encoding of the input

<br>

```py
>>> from pyntor.bracket.pair import Pair
>>> from secrets import randbelow
>>> x = randbelow(100)
>>> y = randbelow(100)
>>> pair = Pair(x, y)
>>> enc = cantor.encode(pair)
>>> enc
6229
```

---

### **PairingFunction.decode(self, n)** <!-- omit in toc -->

> Parameters:
> 
> * pair: *Natural*
> 
>	* The integer to decode.

> Returns:
> 
> * *Pair*
> 
>	* The pair of integers that encodes to the input

<br>

```py
>>> dec = cantor.decode(enc)
>>> dec
(98, 13)
>>> x
98
>>> y
13
```

---

<br>

# 11 Pairing Functions

```py
from pyntor.pairing.functions import *
```

<br>

## Overview

---

`pyntor` currently implements six pairing functions, each a singleton instance.

<br>

## CantorPairing

<br>

```py
def encoder(x, y):
	return (((x + y) * (x + y + 1)) // 2) + y

def decoder(n):
	w = int((sqrt(8 * n + 1) - 1) / 2)
	t = (w * (w + 1)) // 2

	return w - n + t, n - t
```

<br>

## GodelPairing

<br>

```py
def encoder(x, y):
	return (1 << x) * (3 ** y)
	
def decoder(n):
	
	rem = n
	w = 0
	
	while (rem % 6) == 0:
		rem /= 6
		w += 1
		
	if (w & 1) == 0:
		x = int(log2(rem)) + w
		y = w
	else:
		x = w
		y = int(log2(rem)/log2(3)) + w
		
	return x, y
```

<br>

## PeterPairing

<br>

```py
def encoder(x, y):
	max_ = max(x, y)
	min_ = min(x, y)
	f = 0 if max_ == y else 1

	return (max_ ** 2) + (2 * min_) + f

def decoder(n):
	x = int(sqrt(n))
	z = n - (w*w)
	y = z >> 1

	return x, y if (z & 1) == 1 else y, x
```

<br>

## QPairing

<br>

```py
def encoder(x, y):
	return (1 << y) * ((2 * x) + 1) - 1

def decoder(n):
	rem = n + 1
	y = 0

	while (rem & 1) == 0:
		rem >>= 1
		y += 1

	return (w - 1) // 2, y
```

<br>

## RosenbergStrongPairing

<br>

```py
def encoder(x, y):
	max_ = max(x, y)
	return (max_ * (max_ + 1)) + x - y

def decoder(n):
	w = int(sqrt(n))
	z = n - (w * w)

	if z < w:
		x, y = z, w
	else:
		x = w
		y  = (w * (w + 2)) - n

	return x, y
```

<br>

## SquarePairing

<br>

```py
def encoder(x, y):
	max_ = max(x, y)
	n = max_ ** 2

	return (n + y - x) if max_ == y else (n + (2*x) - y)

def decoder(n):
	w = int(sqrt(n))
	z = n - (w * w)

	if z == w:
		x, y = w, z
	elif z < w:
		x, y = (w - z), w
	else:
		x, y = w, (2 * w) - z

	return x, y
```

---

<br>

# Examples

## <u>**A First Example**</u>

```py
>>> from pyntor.pair import Pair, MutablePair
>>> from pyntor.pairing.functions import SquarePairing
>>> from pyntor.bracket.functions import PyramidBracket
>>> 
>>> sqp = SquarePairing()
>>> pyb = PyramidBracket()
>>> 
>>> # Simple Random Pair
>>> 
>>> pair = Pair.random()
>>> enc = sqp.encode(pair)
>>> dec = sqp.decode(enc)
>>> 
>>> pair
(68, 48)
>>> enc
4712
>>> dec
(68, 48)
>>> 
>>> # Random 4-Tuple Pair
>>> 
>>> pair4 = pyb.pair_random(4)
>>> enc4 = sqp.encode(pair4)
>>> 
>>> pair4
((74, 24), (6, 18))
>>> enc4
31370864
>>> 
>>> dec4 = MutablePair(*sqp.decode(enc4))
>>> 
>>> dec4
(5600, 336)
>>> 
>>> dec4.replace(0, sqp.decode(dec4.x))
>>> 
>>> dec4
((74, 24), 336)
>>> 
>>> dec4.replace(1, sqp.decode(dec4.y))
>>> 
>>> dec4
((74, 24), (6, 18))
```

---

## <u>**Encoding Negative Numbers**</u>

```py
>>> from pyntor.folding import fold, unfold
>>> from pyntor.pair import Pair
>>> from pyntor.pairing.functions import CantorPairing
>>> 
>>> cp = CantorPairing()
>>> 
>>> x, y = -37, -68
>>> fx, fy = fold(x), fold(y)
>>> pair = Pair(fx, fy)
>>> 
>>> enc = cp.encode(pair)
>>> dec = cp.decode(enc)
>>> udec = unfold(dec.x), unfold(dec.y)
>>> 
>>> fx
73
>>> fy
135
>>> enc
21871
>>> dec
(73, 135)
>>> udec
(-37, -168)
