- [PairingFunction](#pairingfunction)
	- [Overview](#overview)
	- [Module](#module)
		- [**PairingFunction.\_\_init\_\_(self, encoder, decoder)**](#pairingfunctioninitself-encoder-decoder)
		- [**PairingFunction.encoder**](#pairingfunctionencoder)
		- [**PairingFunction.decoder**](#pairingfunctiondecoder)
		- [**PairingFunction.encode(self, pair)**](#pairingfunctionencodeself-pair)
		- [**PairingFunction.decode(self, n)**](#pairingfunctiondecodeself-n)

<br>

# PairingFunction

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

### **PairingFunction.\_\_init\_\_(self, encoder, decoder)**

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

### **PairingFunction.encoder**

> Decorators:
> 
> @property

> Returns
> 
> * *Callable*
> 
>	* The function that encodes a pair of integers as a single integer

---

### **PairingFunction.decoder**

> Decorators:
> 
> @property

> Returns
> 
> * *Callable*
> 
>	* The function that decodes a single integer into a pair of integers

---

### **PairingFunction.encode(self, pair)**

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

### **PairingFunction.decode(self, n)**

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