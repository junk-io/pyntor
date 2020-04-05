- [BracketFunction](#bracketfunction)
	- [Overview](#overview)
	- [Module](#module)
		- [**BracketFunction.\_\_init\_\_(self, method)**](#bracketfunctioninitself-method)
		- [**BracketFunction.method**](#bracketfunctionmethod)
		- [**BracketFunction.pair(self, sequence)**](#bracketfunctionpairself-sequence)
		- [**BracketFunction.pair_random(self, length, max_value = 100)**](#bracketfunctionpairrandomself-length-maxvalue--100)
		- [**BracketFunction.\_\_call\_\_(self, sequence)**](#bracketfunctioncallself-sequence)
	- [Implementations](#implementations)

<br>

# BracketFunction

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

### **BracketFunction.\_\_init\_\_(self, method)**

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

### **BracketFunction.method**

> Decorators:
> 
> * @property

> Returns:
> 
> * *Callable*
> 
>	* The wrapped transformation function

---

### **BracketFunction.pair(self, sequence)**

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

### **BracketFunction.pair_random(self, length, max_value = 100)**

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

### **BracketFunction.\_\_call\_\_(self, sequence)**

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