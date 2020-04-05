# pyntor

A small [pairing function](https://en.wikipedia.org/wiki/pairing_function) library. Refer to the [doc](https://github.com/junk-io/pyntor/blob/master/doc/api.md) for more details and examples.

## Installation

```py
pip install pyntor
```

## Features

* A `Natural` type representing a nonnegative integer
* Simple `Natural` sequence generation
* Mutable and Immutable `Pair` types
* Straightforward and intuitive pairing mechanism
* 6 pre-implemented pairing functions
* 10 pre-implemented bracket functions
  * These functions take a sequence as input and systematically pairs the elements, either with another element or another pair, ultimately producing a pair as output. Flattening the pair should generate a sequence containing the original elements.
* The ability to encode negative numbers using a simple [folding function](https://mathworld.wolfram.com/FoldingFunction.html)

## Futures

* [ ] Automatic folding and unfolding of negative integers as elements of a `Pair`
* [ ] N-ary decoding of a value based on bracketing method
* [ ] Cartesian product of two sequences
* [ ] Cartesian pairing of two sequences

## A Quick Example

    
    
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
