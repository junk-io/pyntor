- [MutablePair(Pair)](#mutablepairpair)
	- [Overview](#overview)
	- [Module](#module)
		- [**MutablePair.lock(self)**](#mutablepairlockself)
		- [**MutablePair.replace(self, path, new_value)**](#mutablepairreplaceself-path-newvalue)
		- [**MutablePair.\_\_setitem\_\_(self, path, new_value)**](#mutablepairsetitemself-path-newvalue)

<br>

# MutablePair(Pair)

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

### **MutablePair.lock(self)**

> Returns
> 
> * *Pair*
>
>	* An immutable copy of this pair

---

### **MutablePair.replace(self, path, new_value)**

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

### **MutablePair.\_\_setitem\_\_(self, path, new_value)**

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