- [Folding](#folding)
	- [Overview](#overview)
	- [Module](#module)
		- [**fold(value)**](#foldvalue)
		- [**unfold(value)**](#unfoldvalue)

# Folding

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

### **fold(value)**

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

### **unfold(value)**

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