# Day 4: Arrays and Strings

## Arrays
An array is a collection of similar types of elements which have a contiguous memory location. Java array is an object which contains elements of a similar data type.
- Features: Strongly typed, fixed size, 0-indexed.
- Types: Single Dimensional Array, Multidimensional Array.

## Strings
String in Java is an object that represents a sequence of char values. 
- String objects are immutable, meaning once created, their values cannot be changed.
- If we try to alter their value, another object is created.

### String Pool
Strings created using literal quotes are stored in a special memory area called the String Constant Pool.

### StringBuilder and StringBuffer
Since String is immutable, appending to strings in a loop is highly inefficient.
- **StringBuilder**: Mutable, non-synchronized (fast).
- **StringBuffer**: Mutable, synchronized (thread-safe, slower).
