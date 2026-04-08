# Day 60: Advanced OOP Concepts

## Inheritance
Subclass inherits from Superclass using `class Child(Parent):`.
Use `super().__init__()` to call parent constructor.

## Encapsulation
By convention, prepend an attribute with `_` to denote it as "protected", or `__` (double underscore) to invoke name mangling (acting as "private").

## Polymorphism
Same method name but different objects override to provide custom implementation (Duck typing rules).

## Magic / Dunder Methods
Methods wrapped in double underscores like `__str__` (for print), `__len__`, `__add__`.
