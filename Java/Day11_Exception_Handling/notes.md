# Day 11: Exception Handling

## What is an Exception?
An exception is an unwanted or unexpected event, which occurs during the execution of a program i.e at run time, that disrupts the normal flow of the program's instructions.

## Hierarchy
`java.lang.Throwable` -> `Exception` and `Error`.
- **Checked Exceptions**: Classes that directly inherit Throwable except RuntimeException and Error. Checked at compile time (e.g. `IOException`).
- **Unchecked Exceptions**: Classes that inherit RuntimeException. Checked at runtime (e.g. `NullPointerException`).

## Keywords
1. **try**: The code which is prone to exception is placed here.
2. **catch**: Used to handle the exception.
3. **finally**: The block that always executes, regardless of exception occurring or not. Good for resource cleanup.
4. **throw**: Used to explicitly throw an exception.
5. **throws**: Used to declare an exception, indicating that the method might throw it.
