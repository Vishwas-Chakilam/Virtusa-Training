# Day 57: Modules and Packages

## What is a module?
Consider a module to be the same as a code library. A file containing a set of functions you want to include in your application.

## Importing
`import math` -> Use via `math.sqrt()`
`from os import path` -> Use directly via `path.join()`
`import sys as s` -> Alias mapping

## Dunder `__name__`
`if __name__ == "__main__":` ensures that code is executed only if it is run as a script, and not if requested by an import statement.
