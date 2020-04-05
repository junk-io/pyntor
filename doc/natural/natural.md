- [Natural(int)](#naturalint)
	- [Overview](#overview)
	- [Module](#module)
		- [**Natural.RAND_MAX**](#naturalrandmax)
		- [**Natural.\_\_init\_\_(self, value = 0)**](#naturalinitself-value--0)
		- [**Natural.random(cls, max_value = 100)**](#naturalrandomcls-maxvalue--100)
		- [**Natural.naturalize(values)**](#naturalnaturalizevalues)
		- [**Natural.naturals(start, end=None, step=1)**](#naturalnaturalsstart-endnone-step1)
		- [**Natural.random_sequence(length, max_value = 100)**](#naturalrandomsequencelength-maxvalue--100)
		- [**Natural.repeat(value, count)**](#naturalrepeatvalue-count)
		- [**Natural.digits**](#naturaldigits)
		- [**Natural.count(self, digit)**](#naturalcountself-digit)
		- [**Natural.\_\_add\_\_(self, x)**](#naturaladdself-x)
		- [**Natural.\_\_radd\_\_(self, x)**](#naturalraddself-x)
		- [**Natural.\_\_sub\_\_(self, x)**](#naturalsubself-x)
		- [**Natural.\_\_rsub\_\_(self, x)**](#naturalrsubself-x)
		- [**Natural.\_\_mul\_\_(self, x)**](#naturalmulself-x)
		- [**Natural.\_\_rmul\_\_(self, x)**](#naturalrmulself-x)
		- [**Natural.\_\_mod\_\_(self, x)**](#naturalmodself-x)
		- [**Natural.\_\_rmod\_\_(self, x)**](#naturalrmodself-x)
		- [**Natural.\_\_floordiv\_\_(self, x)**](#naturalfloordivself-x)
		- [**Natural.\_\_rfloordiv\_\_(self, x)**](#naturalrfloordivself-x)
		- [**Natural.\_\_and\_\_(self, x)**](#naturalandself-x)
		- [**Natural.\_\_rand\_\_(self, x)**](#naturalrandself-x)
		- [**Natural.\_\_xor\_\_(self, x)**](#naturalxorself-x)
		- [**Natural.\_\_rxor\_\_(self, x)**](#naturalrxorself-x)
		- [**Natural.\_\_or\_\_(self, x)**](#naturalorself-x)
		- [**Natural.\_\_ror\_\_(self, x)**](#naturalrorself-x)
		- [**Natural.\_\_lshift\_\_(self, x)**](#naturallshiftself-x)
		- [**Natural.\_\_rlshift\_\_(self, x)**](#naturalrlshiftself-x)
		- [**Natural.\_\_rshift\_\_(self, x)**](#naturalrshiftself-x)
		- [**Natural.\_\_rrshift\_\_(self, x)**](#naturalrrshiftself-x)
		- [**Natural.\_\_divmod\_\_(self, x)**](#naturaldivmodself-x)
		- [**Natural.\_\_rdivmod\_\_(self, x)**](#naturalrdivmodself-x)
		- [**Natural.\_\_abs\_\_(self)**](#naturalabsself)
		- [**Natural.\_\_pos\_\_(self)**](#naturalposself)
		- [**Natural.\_\_round\_\_(self)**](#naturalroundself)
		- [**Natural.\_\_trunc\_\_(self)**](#naturaltruncself)
		- [**Natural.\_\_floor\_\_(self)**](#naturalfloorself)
		- [**Natural.\_\_ceil\_\_(self)**](#naturalceilself)
		- [**\_\_contains\_\_(self, digit: int)**](#containsself-digit-int)
		- [**\_\_getitem\_\_(self, index: int)**](#getitemself-index-int)
		- [**\_\_len\_\_(self)**](#lenself)

<br>

# Natural(int)

```py
>>> from pyntor.natural import Natural
```
<br>

## Overview

---

`Natural` is a class that represents an indexable non-negative integer. It inherits from `int` and is compatible with any method taking an `int` as input. Arithmetic gives precedence to the *type that can hold the result*.

<br>

## Module

---

### **Natural.RAND_MAX**

> * *Final[Natural]*
> 
>	* The default maximum for random values set to `2`<sup>`31`</sup> `= 2147483648` 
 
---
### **Natural.\_\_init\_\_(self, value = 0)**

> Parameters:
> 
> * value : *int, str, Sequence[int]*
> 
> 	* A non-negative integer. Default is 0

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

### **Natural.random(cls, max_value = 100)**

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

### **Natural.naturalize(values)**

> Decorators:
> 
> * @staticmethod

> Parameters:
> 
> * values: *Iterable*
> 
> 	* A list of non-negative integers

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

### **Natural.naturals(start, end=None, step=1)**

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

### **Natural.random_sequence(length, max_value = 100)**

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

### **Natural.repeat(value, count)**

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

### **Natural.digits**

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

### **Natural.count(self, digit)**

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

### **Natural.\_\_add\_\_(self, x)**
### **Natural.\_\_radd\_\_(self, x)**
### **Natural.\_\_sub\_\_(self, x)**
### **Natural.\_\_rsub\_\_(self, x)**
### **Natural.\_\_mul\_\_(self, x)**
### **Natural.\_\_rmul\_\_(self, x)**
### **Natural.\_\_mod\_\_(self, x)**
### **Natural.\_\_rmod\_\_(self, x)**
### **Natural.\_\_floordiv\_\_(self, x)**
### **Natural.\_\_rfloordiv\_\_(self, x)**
### **Natural.\_\_and\_\_(self, x)**
### **Natural.\_\_rand\_\_(self, x)**
### **Natural.\_\_xor\_\_(self, x)**
### **Natural.\_\_rxor\_\_(self, x)**
### **Natural.\_\_or\_\_(self, x)**
### **Natural.\_\_ror\_\_(self, x)**

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

### **Natural.\_\_lshift\_\_(self, x)**
### **Natural.\_\_rlshift\_\_(self, x)**
### **Natural.\_\_rshift\_\_(self, x)**
### **Natural.\_\_rrshift\_\_(self, x)**

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

### **Natural.\_\_divmod\_\_(self, x)**
### **Natural.\_\_rdivmod\_\_(self, x)**

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

### **Natural.\_\_abs\_\_(self)**
### **Natural.\_\_pos\_\_(self)**
### **Natural.\_\_round\_\_(self)**
### **Natural.\_\_trunc\_\_(self)**
### **Natural.\_\_floor\_\_(self)**
### **Natural.\_\_ceil\_\_(self)**

> Returns:
> 
> * *Natural*
> 
> 	* This integer

---

### **\_\_contains\_\_(self, digit: int)**

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

### **\_\_getitem\_\_(self, index: int)**

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
> 	* The digit in the 10<sup>`index`</sup> position if `index` is a non-negative integer, otherwise the digit in the 10<sup>`len + index` position

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

### **\_\_len\_\_(self)**

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

