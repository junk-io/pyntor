- [NaturalType](#naturaltype)
	- [Overview](#overview)
	- [Module](#module)
		- [**NaturalType.\_\_init\_\_(self, lower_bound = 0, upper_bound = None)**](#naturaltypeinitself-lowerbound--0-upperbound--none)
		- [**NaturalType.lower_bound**](#naturaltypelowerbound)
		- [**NaturalType.upper_bound**](#naturaltypeupperbound)
		- [**NaturalType.range**](#naturaltyperange)
		- [**NaturalType.random(self, max_value=None)**](#naturaltyperandomself-maxvaluenone)
		- [**NaturalType.reset_lower_bound(self, new_value = 0)**](#naturaltyperesetlowerboundself-newvalue--0)
		- [**NaturalType.reset_upper_bound(self, new_value = None)**](#naturaltyperesetupperboundself-newvalue--none)
		- [**NaturalType.\_\_call\_\_(self, value)**](#naturaltypecallself-value)

<br>

# NaturalType

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

### **NaturalType.\_\_init\_\_(self, lower_bound = 0, upper_bound = None)**

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

### **NaturalType.lower_bound**

> Decorators:
> 
> * @property

> Returns:
> 
> * *Natural*
> 
> 	* The lower bound of this type

---

### **NaturalType.upper_bound**

> Decorators:
> 
> * @property

> Returns:
> 
> * *Natural*, *None*
>
>	* The excluded upper bound of this type, if one is set

---

### **NaturalType.range**

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

### **NaturalType.random(self, max_value=None)**

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

### **NaturalType.reset_lower_bound(self, new_value = 0)**

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

### **NaturalType.reset_upper_bound(self, new_value = None)**

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

### **NaturalType.\_\_call\_\_(self, value)**

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
