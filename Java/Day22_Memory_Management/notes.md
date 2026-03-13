# Day 22: Memory Management and GC

## Garbage Collection
Garbage Collection in Java is the process by which programs perform automatic memory management. The JVM checks for unreferenced objects and deletes them to free up memory.

## GC Roots
A GC root is an object that is accessible from outside the heap. Examples: Local variables, active threads, static variables, JNI references. Any object not reachable from a GC root is considered garbage.

## System.gc()
This method suggests that the JVM expends effort toward recycling unused objects to make the memory they currently occupy available for quick reuse. There is NO guarantee that it runs.

## `finalize()`
Called by the garbage collector on an object when GC determines that there are no more references to the object. (Deprecated in newer JDKs, prefer `AutoCloseable` or cleaner mechanisms).
