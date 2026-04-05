# Day 50: Dictionaries and Sets

## Dictionaries (`dict`)
A collection of key-value pairs. Ordered (Python 3.7+), mutable, and does not allow duplicate keys.
- Creation: `d = {"key": "value"}`
- Methods: `.keys()`, `.values()`, `.items()`, `.get(k, default)`.

## Sets (`set`)
A set is a collection which is unordered, unchangeable (but mutable additions), and unindexed. No duplicate members.
- Creation: `s = {1, 2, 3}`
- Very fast for membership testing (`in` operator).
- Standard math ops: Unions (`|`), Intersections (`&`), Differences (`-`).

## Comprehensions
You can build sets and dictionaries efficiently.
`sq_dict = {x: x**2 for x in range(5)}`
