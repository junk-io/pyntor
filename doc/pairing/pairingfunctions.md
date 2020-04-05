- [Pairing Functions](#pairing-functions)
	- [Overview](#overview)
	- [CantorPairing](#cantorpairing)
	- [GodelPairing](#godelpairing)
	- [PeterPairing](#peterpairing)
	- [QPairing](#qpairing)
	- [RosenbergStrongPairing](#rosenbergstrongpairing)
	- [SquarePairing](#squarepairing)

# Pairing Functions

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
