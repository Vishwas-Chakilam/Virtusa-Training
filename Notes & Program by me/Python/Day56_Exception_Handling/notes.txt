# Day 56: Exception Handling

Exceptions alter program flow, preventing crash-outs.

## Syntax Format
```python
try:
    # risky code
except ExceptionType as e:
    # exception handler code
else:
    # executes only if NO exception occurred
finally:
    # executes unconditionally
```

## Raising Exceptions
`raise ValueError("Invalid number provided")`

## Custom Exceptions
Created by inheriting from `Exception` class.
