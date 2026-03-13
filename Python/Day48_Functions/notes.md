# Day 48: Functions

## Defining a Function
A block of reusable code defined using the `def` keyword.
- Parameters map to arguments passed during calling.
- Return values using `return`. If no return is present, returns `None`.

## Arguments
- **Positional**: Expected in same order.
- **Default/Keyword**: Provide default values (`def greet(name="User"):`).
- **Arbitrary**:
  - `*args`: Collects positional args into a tuple.
  - `**kwargs`: Collects keyword args into a dictionary.

## Lambda Functions
Small anonymous functions defined by `lambda x: x*2`. Used often with functional methods like `map()`, `filter()`.
