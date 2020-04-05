- [Pair](#pair)
	- [Overview](#overview)
	- [Module](#module)
		- [**Pair.\_\_init\_\_(self, x, y)**](#pairinitself-x-y)
		- [**Pair.from_tuple(cls, pair)**](#pairfromtuplecls-pair)
	- [>	* A copy of the pair as a `Pair`](#blockquote-ul-lia-copy-of-the-pair-as-a-pairli-ul-blockquote)
		- [**Pair.random(cls, max_value_x = 100, max_value_y = 100)**](#pairrandomcls-maxvaluex--100-maxvaluey--100)
		- [**Pair.x**](#pairx)
		- [**Pair.y**](#pairy)
		- [**Pair.copy(self)**](#paircopyself)
		- [**Pair.count(self)**](#paircountself)
		- [**Pair.depth_of_x(self)**](#pairdepthofxself)
		- [**Pair.depth_of_y(self)**](#pairdepthofyself)
		- [**Pair.flatten(self)**](#pairflattenself)
		- [**Pair.is_natural(self)**](#pairisnaturalself)
		- [**Pair.\_\_getitem\_\_(self, key)**](#pairgetitemself-key)
		- [**Pair.\_\_iter\_\_(self):**](#pairiterself)
		- [**Pair.\_\_reversed\_\_(self):**](#pairreversedself)
	- [Implementations](#implementations)

<br>

# Pair

```py
>>> from pyntor.pair import Pair
```

<br>

## Overview

---

A `Pair` is a tuple of two elements 'x' and 'y' that can either be a non-negative integer or another `Pair`.

<br>

## Module

### **Pair.\_\_init\_\_(self, x, y)**

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

### **Pair.from_tuple(cls, pair)**

> Parameters:
> 
> * pair: *Tuple*, *Pair*
> 
> 	* A 2-tuple where the elements are either `Natural` numbers or another 2-tuple

> Returns:
> 
> * *Pair*
> 
>	* A copy of the pair as a `Pair`
---

### **Pair.random(cls, max_value_x = 100, max_value_y = 100)**

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

### **Pair.x**

> Decorators:
> 
> * @property

> Returns:
> 
> * *Natural*, *Pair*
> 	* The first element of this pair

---

### **Pair.y**

> Decorators:
> 
> * @property

> Returns:
> 
> * *Natural*, *Pair*
> 	* The second element of this pair

---

### **Pair.copy(self)**

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

### **Pair.count(self)**

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

### **Pair.depth_of_x(self)**

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

### **Pair.depth_of_y(self)**

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

### **Pair.flatten(self)**

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

### **Pair.is_natural(self)**

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

### **Pair.\_\_getitem\_\_(self, key)**

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

### **Pair.\_\_iter\_\_(self):**

> Returns:
> 
> The first element, then the second

---

### **Pair.\_\_reversed\_\_(self):**

> Returns:
> 
> The second element, then the first

---

<br>

## Implementations

---

* `MutablePair`