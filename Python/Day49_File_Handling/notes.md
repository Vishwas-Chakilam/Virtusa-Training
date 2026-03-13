# Day 49: File Handling

## File Operations
We use `open(file, mode)` to return a file object.
Modes: `r` (read), `w` (write dictating overwrite), `a` (append), `x` (create).

## Context Managers (`with` statement)
It is highly recommended to use the `with` keyword to open a file. It acts as a context manager and guarantees the file is properly closed, even if an exception is raised.

## `json` Module
JSON is built-into Python, allowing dict/list serialization via `json.dump()` / `json.dumps()`, and decoding via `json.load()` / `json.loads()`.
