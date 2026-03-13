# Day 14: Threading

## Multithreading in Java
Multithreading is a process of executing multiple threads simultaneously.
Java provides built-in support for multithreading.

## Thread Lifecycle
1. **New**: Created but not started.
2. **Runnable**: Started and executing, waiting for CPU cycle.
3. **Running**: CPU is actively executing the thread.
4. **Waiting/Blocked**: Waiting for resource lock.
5. **Terminated/Dead**: Finished execution.

## Creating a Thread
1. Extending the `Thread` class.
2. Implementing the `Runnable` interface.

## Synchronization
When two or more threads need access to a shared resource, they need some way to ensure that the resource will be used by only one thread at a time. The process by which this is achieved is called synchronization (using the `synchronized` keyword).
