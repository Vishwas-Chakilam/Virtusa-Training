# Day 58: Regular Expressions

## The `re` Module
Regular expressions are powerful string matching sequences.
- `re.match(p, s)`: Checks only the beginning.
- `re.search(p, s)`: Scans for first match.
- `re.findall(p, s)`: Returns all non-overlapping matches as list.
- `re.sub(p, repl, s)`: Replace matches.

## Basic Syntax
- `\d` = Digit
- `\w` = Word character (a-z, A-Z, 0-9, _)
- `^` = Start of string, `$` = End of string
- `.` = Any character except newline
- `+` = One or more, `*` = Zero or more
