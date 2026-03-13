# Day 12: Enums, Annotations, and File I/O

## Enums
An enum is a special "class" that represents a group of constants (unchangeable variables, like final variables).
It improves type safety and can be used in switch statements.

## Annotations
Annotations provide data about a program that is not part of the program itself.
- `@Override`: Checks if the method is overridden correctly.
- `@Deprecated`: Marks the method as deprecated.
- `@SuppressWarnings`: Instructs compiler to suppress specific warnings.

## File I/O
The `java.io` package contains nearly every class you might ever need to perform input and output (I/O) in Java. All these streams represent an input source and an output destination.
- **Byte Streams**: Used for handling input and output of bytes (8-bit bytes). (`FileInputStream`, `FileOutputStream`).
- **Character Streams**: Used for handling input and output of characters (16-bit Unix). (`FileReader`, `FileWriter`).
